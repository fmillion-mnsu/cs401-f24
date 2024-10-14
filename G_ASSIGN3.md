# Group Assignment 3

This is the final assignment for this course! In this assignment you will build a Dockerfile along with an entrypoint and healthcheck script for a simple application. 

## The Application

The application provided is a simple Web server. The server has the following endpoints:

* `/`: Returns `Hello World`.
* `/stop`: Causes the application to "stop". The server does not actually shut down, it simply stops responding correctly to any API endpoint other than `/start`. *This allows you to test your healthcheck script, as the `/check` URL will not return the expected response when the server is stopped..*
* `/start`: Return the server to a working state.
* `/cpu.json`: Returns information about the system CPU in a JSON format.
* `/cpu`: Return a formatted web page with information about the system CPU.
* `/check`: If the server is running, returns `OK`. *Use this for your healthcheck script as per the instructions below.*
* `/log`: Get a list of all logged accesses to the API, in JSON format.

## Requirements

Prepare a Dockerfile, Entrypoint and HealthCheck script for the application in this repository located under the directory `Assignment3`. The application is a simple Python application that implements a simple Flask-based website. 

Within the `Assignment3` folder, you will see the file `app.py`, which is the application; the file `dbsetup.py` which is the database setup script, and a `requirements.txt` file.

> If you aren't familiar, a `requirements.txt` file is used by Python's `pip` package manager to specify what libraries are required by a Python application. You'll use it during the build process.

Your Dockerfile must incorporate the following characteristics:

* **Use an appropriate base image.** This code should work with any modern version of Python.
* **Install the `curl` command line utlity.** One of the requirements for your `HEALTHCHECK` script will use `curl`. 
  * Hint: The base `python` images use Debian as the base OS, so you will use the `apt` package manager to do installations.
* **Avoid unnecessary files in the final container image.** You can accomplish this in many ways, such as using `tmpfs` on cache directories, using `&&` to chain commands together, or using specific command line switches for the installation tools to prevent caching of files inside the container. Do your research on this - choose whichever method you prefer, but the final container should *not* contain any installation caches!
* **Support optimizations for build layer caching.** In particular, copy the `requirements.txt` file into the container independently, run `pip install` as appropriate, and then copy in the source code. This minimizes the need to rerun `pip install` if the requirements file has not changed.
* **Create a user account within the container which the program will run as.** The `useradd` command is the one you're looking for - it supports command line options for automating the process.
* **Make sure you have a step that ensures that your entrypoint and healthcheck scripts are executable.** Hint: `chmod +x`.
* **Use `USER` to run the application as a user other than `root`.** You need to do this *after* creating the user account as above.
* **Use `EXPOSE` to indicate which port the service listens on.** The web server inside the container listens on port **5000**.
* **Implement both healthcheck and entrypoint scripts.** More on this in the next section.

### Entrypoint Script

Your `entrypoint.sh` script should be written in Bash and must accomplish the following:

* **Check whether the user has mounted persistent storage on `/data`.** There's a few ways you can do this, but one idea is to add a step in your Dockerfile that creates an empty file in `/data`, and then your entrypoint script checks whether that file exists. If the user did mount storage on `/data`, the file you created should *not* be present.
* **Change the ownership of `/data` and all files within it to the user you created for running the application.** The `chown` command is the one you're looking for to do this. Look at the manual page or research how to have the command be recursive.
* **Create the database file in `/data`, but ONLY if it has not been done before.** The Python file `dbsetup.py` can be run to accomplish this. *However,* you should **not** seed the database if it already exists! You need to devise and implement a solution for checking whether the database has been seeded each time the entrypoint runs, and skip the process if it's already done.
* **Use `exec` to start the `app.py` program.** This should be the last step in your entrypoint script.

### Healthcheck script

Your `healthcheck.sh` script should do the following:

* **Use the `curl` command to try to access the URL `http://localhost:5000/check`.** Simply run `curl http://localhost:5000/check`.
  * If this URL returns the string `OK`, the service is up. Return an appropriate *success* return code.
  * If the URL access fails, or does not contain the string `OK`, the healthcheck should fail. Return an appropraite *failing* return code.

It's up to you to figure out how to check the output of the `curl` command!

## Deliverable

Your deliverable is simply your `Dockerfile` and accompanying `.sh` script files for the entrypoint and healthcheck. You don't need to include the source files (the Python scripts).

This is a **group** project - only **one** submission per group is required.

The due date for this assignment is **Wednesday, October 23** at **11:59 PM**.

## Resources

This assignment only scratches the surface of the breadth of information available via simple interfaces such as the files in `/proc` and `/sys`. You can install the package `lshw` if you want to try a very comprehensive system information tool that extracts a large amount of information via these interfaces. 

Also note that nearly every other tool that presents information about your system is using these interfaces to obtain that information. Commands such as `free`, `top`/`htop`, `uptime`, `uname` and so on are all simply accessing the data provided by these virtual files!
