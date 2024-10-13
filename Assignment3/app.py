import json
import os.path
import platform
import sqlite3
import time

from flask import Flask, Response, render_template_string
from flask.views import MethodView

app = Flask(__name__)

API_IS_ACTIVE = True

##### Utility functions #####

def log(endpoint):
    ctx = sqlite3.connect("/data/log.sqlite3")
    cur = ctx.cursor()

    cur.execute("INSERT INTO log (date, endpoint) VALUES (?, ?)", (time.time(), endpoint))
    
    ctx.commit()
    cur.close()
    ctx.close()

def split_on_empty_strings(lst):
    result = []
    current_sublist = []
    for item in lst:
        if item.strip() != '':
            current_sublist.append(item)
        else:
            if current_sublist:
                result.append(current_sublist)
                current_sublist = []
    if current_sublist:
        result.append(current_sublist)
    return result

def convert_number(v):
    try:
        return int(v)
    except ValueError:
        try:
            return float(v)
        except ValueError:
            return v

##### Get CPU info function #####
def get_cpu_info():

    # Read /proc/cpuinfo into line array
    with open('/proc/cpuinfo', 'r') as f:
        lines = f.readlines()
    
    # There are empty lines in the array. Split into an array of arrays split on the blank lines.
    lines = split_on_empty_strings(lines)

    # Get the first array of the split array
    cpu_info = lines[0]

    # Clean the list
    cpu_info = [x.strip() for x in cpu_info]            # remove newlines
    cpu_info = [x.replace("\t","") for x in cpu_info]   # remove tabs
    
    # Make a dictionary based on the strings
    cpu_info_dict = {x[0].strip(): convert_number(x[1].strip()) if len(x) > 1 else '' for x in [y.split(":",2) for y in cpu_info]}

    # explicit: convert any value of "yes" to a boolean True, and any of a "no" to a boolean False.
    cpu_info_dict = {x[0]: True if x[1] == "yes" else False if x[1] == "no" else x[1] for x in cpu_info_dict.items()}

    # explicit: convert a few flag values to lists
    for key in ["flags","vmx flags","bugs"]:
        if key in cpu_info_dict:
            cpu_info_dict[key] = sorted(cpu_info_dict[key].split(" "))

    # explicit: convert cache size to bytes
    cpu_info_dict["cache size"] = int(cpu_info_dict["cache size"].split(" ",2)[0]) * 1024

    del(cpu_info_dict["core id"])
    del(cpu_info_dict["processor"])
    cpu_info_dict["threads"] = len(lines)

    return cpu_info_dict
    
class HelloWorldView(MethodView):
    def get(self):

        global API_IS_ACTIVE
        if not API_IS_ACTIVE:
            return Response(status=500)

        return Response("Hello World", content_type='text/html')

class EnableAPIView(MethodView):
    def get(self):
        global API_IS_ACTIVE
        API_IS_ACTIVE = True
        return Response(json.dumps({"state":True}), content_type='application/json')

class DisableAPIView(MethodView):
    def get(self):

        global API_IS_ACTIVE
        if not API_IS_ACTIVE:
            return Response(status=500)

        API_IS_ACTIVE = False
        return Response(json.dumps({"state":False}), content_type='application/json')

class CheckView(MethodView):
    def get(self):

        global API_IS_ACTIVE
        if not API_IS_ACTIVE:
            return Response(status=500)

        return Response("OK", content_type='text/plain')

class CPUView(MethodView):
    def get(self):
        html_content = '''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Dictionary Representation</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 20px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-bottom: 20px;
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #f2f2f2;
                }
                .nested {
                    padding-left: 20px;
                    border-left: 2px solid #ddd;
                }
            </style>
        </head>
        <body>
            <h1>Your CPU</h1>
            {{ table|safe }}
        </body>
        </html>
        '''

        def dict_to_html(d):
            if isinstance(d, dict):
                html = '<table>'
                for key, value in d.items():
                    html += f'<tr><th>{key}</th><td class="nested">{dict_to_html(value) if isinstance(value, (dict, list)) else value}</td></tr>'
                html += '</table>'
                return html
            elif isinstance(d, list):
                html = '<ul>'
                for item in d:
                    html += f'<li>{dict_to_html(item)}</li>'
                html += '</ul>'
                return html
            else:
                return str(d)

        table_html = dict_to_html(get_cpu_info())
        return Response(html_content.replace('{{ table|safe }}', table_html), content_type='text/html')

class CPUJsonView(MethodView):
    def get(self):

        global API_IS_ACTIVE
        if not API_IS_ACTIVE:
            return Response(status=500)

        return Response(json.dumps(get_cpu_info()), content_type='application/json')

app.add_url_rule('/', view_func=HelloWorldView.as_view('hello_world'))
app.add_url_rule('/start', view_func=EnableAPIView.as_view('enable_api'))
app.add_url_rule('/stop', view_func=DisableAPIView.as_view('disable_api'))
app.add_url_rule('/check', view_func=CheckView.as_view('check'))
app.add_url_rule('/cpu', view_func=CPUView.as_view('cpu'))
app.add_url_rule('/cpu.json', view_func=CPUJsonView.as_view('cpu_json'))

if __name__ == '__main__':

    # Check whether the data file /data/log.sqlite3 exists.
    if not os.path.isfile("/data/log.sqlite3"):
        print("The database is not initialized!")
        exit(1)

    # Detect if running on Linux; if not, exit with failure
    if platform.system() != 'Linux':
        print("This script is only supported on Linux")
        exit(1)

    app.run(debug=False, host='0.0.0.0', port=5000)