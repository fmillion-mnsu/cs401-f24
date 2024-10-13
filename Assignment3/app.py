import json
import platform

from flask import Flask, Response
from flask.views import MethodView

app = Flask(__name__)

API_IS_ACTIVE = True

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

def get_cpu_info():

    # Read /proc/cpuinfo into line array
    with open('/proc/cpuinfo', 'r') as f:
        lines = f.readlines()
    
    # There are empty lines in the array. Split into an array of arrays split on the blank lines.
    lines = split_on_empty_strings(lines)

    # Get the first array of the split array
    cpu_info = lines[0]

    print(cpu_info)
    
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

app.add_url_rule('/', view_func=HelloWorldView.as_view('hello_world'))
app.add_url_rule('/start', view_func=EnableAPIView.as_view('enable_api'))
app.add_url_rule('/stop', view_func=DisableAPIView.as_view('disable_api'))
app.add_url_rule('/check', view_func=CheckView.as_view('check'))

if __name__ == '__main__':

    # Detect if running on Linux; if not, exit with failure
    if platform.system() != 'Linux':
        print("This script is only supported on Linux")
        exit(1)

    get_cpu_info()
    exit(0)
    app.run(debug=True, host='0.0.0.0', port=5000)