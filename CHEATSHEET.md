# Linux Cheat Sheet

We will develop and expand this document throughout the quarter - consider it your "holy grail" of quick reference for the concepts taught in this course!

## Commands

### Basic Navigation

* `pwd`: Show the current directory
* `cd`: Change directory
  * On its own: change to your *home directory*
  * With a directory as a parameter: go to that directory
* `ls`: List files in the current or another directory
  * `ls -l`: List files with details

### Working with files

* `cat`: Print the contents of a file
* `cp`: Copy a file
* `mv`: Move a file
* `rm`: Remove a file
  * `rm -r`: Remove a directory *recursively*
* `mkdir`: Make a directory
* `rmdir`: Remove an (empty) directory
* `chown`: Change the owner of a file or diretory
* `chmod`: Change the mode (permissions) of a file or directory

### Security

* `id`: Show your current user ID, group IDs, etc.
* `sudo`: Run a command as the root or another user.
  * Use `sudo -u <user> <command>` to run a command as a specific user. Omit the `-u <user>` to run as root.

### Getting system information

* `lscpu`: Show information about your CPU
* `free`: Show overall memory information
* `df`: Show disk usage and free space
* `lsblk`: List all **block devices** in the system

## Compressed Files

* Create a `.tar` archive of one or more files and/or directories using `tar`: `tar -c -f <output_file.tar> <file/dir> [<file/dir> ...]`
* Same as above, but compress the files using `gzip`:
  * `tar -c -z -f <output_file.tar.gz> <file/dir> [<file/dir> ...]`
  * Or using a pipe and redirection: `tar -c -f - <file/dir> [<file/dir> ...] | gzip - > output_file.tar.gz`
* Same as above, but compress using `xz` - very good compression, but slower for very large files: `tar -c -f - <file/dir> [<file/dir> ...] | xz -c - > output_file.tar.xz`
* Extract the contents of a `.tar` file (most modern `tar` versions will detect compressed tarfiles automatically): `tar -x -f <tarfile.tar>`
* Extract the contents of a compressed `.tar` file using a pipe, in case `tar` doesn't auto-detect the compression:
  * gzip: `gzip -d -c <tarfile.tar.gz> | tar -x -f -`
  * bzip2: `bzip2 -d -c <tarfile.tar.bz2> | tar -x -f -`
  * xz: `xz -d -c <tarfile.tar.xz> | tar -x -f -`
* Show a **list** of files in a `.tar` archive without actually extracting them: replace `-x` with `-t` on any command that extracts a tarfile

### Switches for `tar`

Add these to the `tar` command prior to the `-f` option to affect `tar`'s operation as follows:

* `-v`: Display all filenames when compressing or decompressing on standard error. Compatible with pipes.
* `-C <dir>`: Change directory to `<dir>` before compressing or decompressing. Helpful when compressing files to ensure the path stored in the `tar` file is correct

## `nano` Editor

* `Ctrl+X`: exit Nano. It will ask you to save the file if it has been changed.
* `Ctrl+K`: delete the current line and put it on the clipboard. (If pressed repeatedly, copies each additional line to the clipboard. If you change location however, the clipboard is cleared before copying.)
* `Ctrl+U`: Paste the clipboard contents
* `Ctrl+F`: Search in file
* `Ctrl+O`: Save current file without exiting Nano
* `Right Alt (Meta) + U`: Undo command

## Bash Scripting

### Piping and Redirection

* Take output of one command and send it to input of next command: `|` (shift+backslash) Also known as the pipe character or "vertical bar"
* Write the output of the final command in a chain to a file, **overwriting** the file if it exists: `>`
* Write the output of the final command to a file, appending to the file if it exists: `>>`
* Send the contents of a file to standard input of the first command in a chain: `<`

#### Examples for Pipes

* "Page" the output of a command so that it can be viewed page by page rather than scrolling the buffer: `[your command] | less`
  * `less` is a "pager" which stores all of the incoming data and presents it to you in a navigable form. In `less`, you can use the space bar to advance a page and the `b` key to back up a page. Press `q` to quit, or `h` for a help screen with several other options.

#### Advanced: Process Substitution

Process substitution lets you treat the output of a command as if it were a file being provided to another application.

Syntax: `<(command)`

Example - compare directory listings of two directories: `diff <(ls dir1) <(ls dir2)`

### Variables and Expansions

* Assign a string without spaces to a variable named `MY_VAR`: `MY_VAR=thisIsAString`
  * Hint: **No** spaces surrounding the `=`.
* Assign a string *with* spaces to a variable named `MY_VAR`: `MY_VAR="This is a string"`
* Assign a literal string that contains characters that may have special meaning (such as `$` or `!`) to a variable named `MY_VAR`: `MY_VAR='I made $1000 today!'`
* Include the value of a variable inside of another string:
  * Variable expansion is accomplished using the `$`.
  * `$MY_VAR` - assuming that `MY_VAR` is unambiguous
  * `${MY_VAR}` - to explicitly indicate the variable name. Useful in scenarios like this: `Now creating file${FILE_NUM}.` -> (for example) `Now creating file1.`
* Include the *result* of running a command within a string: `$(<command>)`
  * Example: `echo $(pwd)` (prints the current working directory, which is returned by `pwd`)

> Expansions can be used anywhere within bare strings or within double-quoted strings. For example, you could assign a string containing the current directory to a variable in one go with: `MSG="The current directory is $(pwd)."`

#### Sequences

* Generate a sequence of numbers or characters: `{START..END}`
  * Example: `{1..10}` generates the numbers between 1 and 10 inclusive.
  * Example: `{a..z}` generates all of the letters of the alphabet in lowercase.
  * Example: `{001..010}` returns the numbers between 1 and 10 inclusive, padded with zeroes to be three digits long
  * Sequences can be done in reverse by putting a larger value in `START` and a smaller one in `END` - example: `{5..3}` returns `5 4 3`.
* Generate a sequence with a specific **step** (skip every *step* value): `{START..END..STEP}`
  * Example: `{1..10..2}` returns `1 3 5 7 9`

> If you include other static characters in the same **token** as the sequence expansion, those characters will be included in each iteration of the sequence.
>
> For example: `dir{1..5}` returns `dir1 dir2 dir3 dir4 dir5`

> You can combine multiple expansions; they will be combined in a many-to-many fashion.
>
> For example: `{1..3}{a..c}` returns `1a 1b 1c 2a 2b 2c 3a 3b 3c`

#### String manipulation

* Get a substring of a string:
  * One or more characters starting at a given position: `${VARIABLE:INDEX:NUM_CHARS}`
  * From a character to the end of the string: `${VARIABLE:INDEX}`
  * From a character counting from the end of the string backwards: `${VARIABLE: -INDEX}`
* Search and replace:
  * Replace the **first** occurrence of a string in a variable with another string: `${VARIABLE/SEARCH/REPLACE}`
    * Example: `${VARIABLE/Hello/Goodbye}`
  * Replace **all** occurrences of a string in a variable with another string: `${VARIABLE//SEARCH/REPLACE}`
* Remove start/end strings from a string:
  * Remove a given string or wildcard matched string from the end of a string:
    * Lazy (remove as little as possible): `${VARIABLE%REMOVE_STRING}` - example: `${FILENAME%.jpg}` removes `.jpg` from the end of a filename if it ends with `.jpg`
    * Eager (remove as much as possible): `${VARIABLE%%REMOVE_STRING}`
  * Remove a given string or wildcard matched string from the beginning of a string:
    * Lazy (remove as little as possible): `${VARIABLE#REMOVE_STRING}` - example: `${PATH#/}` to remove leading slashes from a path
    * Eager (remove as much as possible): `${VARIABLE##REMOVE_STRING}`
* Return the value of a variable, or a default string if the variable is empty: `${VARIABLE:-DEFAULT}`
* Return a specific static value if a variable is not empty, otherwise return an empty string: `${VARIABLE:+STATIC_VALUE}`

#### Internal variables

These variables are defined by Bash and are available in scripts:

* Positional variables `$1`, `$2`, ...: Contains values passed either into the script on the command line or into a function
* `$#`: Contains the number of parameters passed to the script or function
* `$*`: Contains all parameters as a single, non-iterable string
* `$@`: Contains all parameters in an iterable string, split by space (or by `$IFS`)
* `$?`: Contains an integer representing the return value of the last executed command
* `$IFS`: Contains the character used to split the parameters to functions. Defaults to a space. Can be set to change the separator prior to e.g. calling a function
* `$RANDOM`: Always returns a random number between 0 and 32767.

#### Arrays

* Defina an array from static values: `ARRAY_VARIABLE=("val1" "val2" ...)`
  * Python equivalent: `array_variable=["val1","val2",...]`
* Get the number of items in an array: `${#ARRAY_VARIABLE[@]}`
  * Python equivalent: `str(len(array_variable))`
* Get one element from an array: `${ARRAY_VARIABLE[INDEX]}`
* Replace the value of an array element in-place: `${ARRAY_VARIABLE[INDEX]}=NEW_VALUE`
* Delete an item from the array by index: `unset ${ARRAY_VARIABLE[INDEX]}`
  * Python equivalent: `del array_variable[index]`
* Get the entire contents of an array for iterating, such as in a `for` loop: `${ARRAY_VARIABLE[@]}`

### Conditionals

**Key point:** In Bash, **return codes** are the only thing used for Boolean truthiness. `0` represents success or `true`, while any nonzero value between `1` and `255` represents failure or `false`.

The `test` command, also usable as the alias `[`, is most commonly used with `if` or `while` blocks to perform the check on a value.

* `if` Syntax: `if <condition>; then <statements>; fi`
* `while` Syntax: `while <condition>; do <statements>; done`

#### Common tests using `[`:

For these examples, `$VAR1` and `$VAR2` represent arbitrary variables - replace them with yours (or with something else, such as a `$( )` statement!).

* Is a string equal to another string: `[ $VAR1 = $VAR2 ]`
* Is an integer equal to another integer: `[ $VAR1 -eq $VAR2 ]`
* Are two integers non-equal: `[ $VAR1 -ne $VAR2 ]`
* Is `VAR1` greater than `VAR2`: `[ $VAR1 -gt $VAR2 ]` (equivalent of `VAR1 > VAR2`)
* Is `VAR1` greater than *or equal to* `VAR2`: `[ $VAR1 -ge $VAR2 ]` (equivalent of `VAR1 >= VAR2`)
* Is `VAR1` less than `VAR2`: `[ $VAR1 -lt $VAR2 ]` (equivalent of `VAR1 < VAR2`)
* Is `VAR1` less than *or equal to* `VAR2`: `[ $VAR1 -le $VAR2 ]` (equivalent of `VAR1 <= VAR2`)
* Is `VAR1` a readable file: `[ -f $VAR1 ]`
* Is `VAR1` a directory: `[ -d $VAR1 ]`
* Is `VAR1` a *writable* file: `[ -w $VAR1 ]`
* Is `VAR1` an *exectuable* file (a script or program): `[ -x $VAR1 ]`
* Is `VAR1` non-empty: `[ -z $VAR1 ]`

#### Example code

`if` statement:

    MY_VAR=1
    if [ $MY_VAR -eq 1 ]; then
      echo "My variable is equal to 1."
    else
      echo "My variable is not equal to 1."
    fi

`while` loop:

    BOTTLES=99
    while [ $BOTTLES -gt 0 ]; do
      echo "$BOTTLES bottles of water in the fridge,"
      echo "$BOTTLES bottles of water..."
      echo "Take one out and gulp it down,"
      BOTTLES=$(($BOTTLES - 1))
      echo "$BOTTLES bottles of water in the fridge."
      echo
    done

### Control flow

#### `if` statement

Syntax: 

    if CONDITION; then
      STATEMENTS
    fi

See the [Conditionals](#conditionals) section for conditions you can use in an `if` statement. 

> Remember that in `bash`, a value of `0` is a **truthy** value.

#### `for` loop

Syntax:

    for ITERATION_VARIABLE in SEQUENCE; do
      STATEMENTS
    done

The `SEQUENCE` can be any of these:

* an array
* a sequence generated using `{..}` syntax
* a space-separated list of static values

#### `while` loop

Syntax:

    while CONDITION; do
      STATEMENTS
    done

#### `case` block

Similar to `switch` in other languages.

Syntax:

    case "$VALUE" in
      value)
        STATEMENTS
        ;;
      another_value)
        STATEMENTS
        ;;
      *)
        DEFAULT_STATEMENTS
        ;;
    esac

The cases can be static values or wildcard expansions. Using `*` as a case is effectively equivalent to a `default` case in other languages.

Cases are evaluated in the order listed. The first case to match is the one executed. (This means that if `*)` is your first case, it is the only case that will ever be executed!)

> You can use `|` to do a logical OR - to match on multiple values. For example: `*.wav | *.flac)`

### Functions

Functions have unique properties in Bash:

* They cannot define specific parameters
* They cannot directly return any value other than a numeric return code (either `0` or nonzero up to `255`)
* They act as indepenent scripts, with the exception being that an `exit` statement inside of a function in the same script file will terminate the entire script, not just that function
* Parameters given to the script are accessed via the positional variables `$1`, `$2`, etc.
* Functions are called *without* parentheses.
* The name of the function may or may not include `()`, but they are ignored if given. No parameters or values may be inside the `()`.

Examples:

**Defining and using a simple function**

    function print_message() {
      echo "Hello world"
    }

    print_message

**Using positional parameters**

    function show_param() {
      echo "You passed in this parameter: $1"
    }

    show_param Hello

**"Returning" a value from a function and assigning it to a variable**

    function return_value() {
      echo "This is the returned value."
    }

    FUNC_VALUE=$( return_value )
    # Note how this uses execution expansion to get the value "echo"ed in the function

**Writing a function that returns a return code and using it in an if block**

    function enough_params() {
      if [ $# -eq 4 ]; then
        return 0 # four parameters given
      else
        return 1 # incorrect number of parameters given
      fi
    }

    if $(enough_params 1 2 3 4); then
      echo "There are four values."
    fi

    if $(enough_params 1 2 3); then
      echo "This shouldn't happen!"
    else
      echo "There are not four values."
    fi

### Approximating a try/catch block

We can exploit the evaluation of Boolean operators to create an effective try-catch block.

Example:

    function error_handler() {
      echo "Something went wrong."
    }

    function_that_might_fail || error_handler

### Aliases

Aliases are simple 1:1 expansions. They are useful for making commands faster to type and for providing default options to a command.

* To set an alias: `alias CMD=VALUE`
  * example: `alias gita="git add -A"`
* To list currently defined aliases: `alias`
* To unset an alias: `unalias CMD`

### Importing other scripts

The `source` command (Bash specific) or the `.` command (generic) will load and execute another script in the *same* shell.

> Directly executing a script with e.g. `./script.sh` will launch a *new* shell for that script; anything defined in the current shell won't be passed forward, nor will anything created in the new shell be available to the shell you executed from.

A common use for `source` is to create a separate script file with only functions defined. You can then `source` that file to get access to its functions in any other script.

### "Here" Documents

Similar to triple-quoted multi-line strings in Python.

Syntax: 

    <<DELIMITER
    string
    string
    ...
    DELIMITER

`DELIMITER` can be any string without spaces. Commonly used is `EOF`.

### Parsing command-line options

The `getopts` command creates an interation over the parameters given on the script's invocation. Each time it is run, it returns one option. 

It can be used in a while loop, as it returns a nonzero value when there are no more arguments to return, to iterate over all options provided.

Example Syntax: 

    while getopts "vy" opt; do
      case $opt in
        v) echo "Verbose mode selected." ;;
        y) echo "No confirmation selected." ;;
        \?) echo "unknown option $opt"; exit 1 ;;
      esac
    done

To accept a parameter for an option, add a `:` after that character in the list. For example: `while getopts "vf:" opt; do ...` When you do this, the parameter will be available in the variable `OPTARG`.

This command shifts off all parsed command line arguments, leaving the positional variables pointing to only those parameters not part of command line switches: `shift $((OPTIND - 1))`

## Docker

Docker is a popular implementation of *containers*.

* **Run a container**: `docker run <parameters> <image_name> <arguments>`
  * `<parameters>` is one or more options. See below.
  * `<image_name>` is the name of a Docker image. If you have built an image, it is the name you provided after `-t` on `docker build`. Otherwise, Docker will try to download the specified image by name from Docker Hub, or if a full URL is provided, the server at the given URL.
  * `<arguments>` is optional. Arguments given here are passed to the entrypoint of the container as command line arguments.
* **View list of containers**: `docker ps`
  * View *all* containers, even stopped ones: `docker ps -a`
* **Stop a container by name**: `docker stop <container>`
* **Restart a container by name**: `docker restart <container>`
* **Remove a container by name, assuming it is stopped**: `docker rm <container>`
* **Show messages from a container**: `docker logs <container>`
  * If you use `docker logs -f <container>`, the process will not exit and will instead continue to print ongoing messages from the application. Press Ctrl+C to exit the log viewing session; the container will be unaffected.
* **Build a Docker container**: `docker build -t <image_name> <path>`
  * `<image_name>` will be assigned to the built container image. You can use this as the `<image_name>` parameter in `docker run`.
  * `<path>`: The path containing the Dockerfile along with any supporting files. Using `.` is common if you are currently in the directory containing the project.
  * You can add the `--no-cache` option prior to the path if you want to instruct Docker *not* to use any cached layers, even if it would be otherwise possible.

### Docker Run parameters

* `--name`: Provide your own name for the container, for use in `docker stop`, `docker rm`, etc. If you do not provide this parameter, Docker selects a random container name by concatenating an adjective with the name of a famous scientist.
  * Docker container names must consist of only lowercase alphanumeric characters, numbers, underscore (`_`), and hyphen (`-`).
* `-d`: Run the container in the background and return to the prompt immediately.
* `-it`: Run the container in the foreground, **i**nteractively. 
  * In this mode, if you press Ctrl+C to stop the application, the container will exit.
  * For Assignment 3, you should not need to run the container in the foreground.
* `-p <host_port>:<container_port>`: Forward a host network port to a port within the container. 
  * For example, if a service is running in the container on port 3000, but you want that service available on your system at port 1000, you would issue the parameter `-p 1000:3000`.
  * `-p` can be given multiple times to forward multiple ports.
* `-v` <host_path>:<container_path>`: Map a host directory or file into the container at a given path.
  * For example, if you wish the path `/home/user/data` to be available within the container at `/data`, you would issue the parameter `-v /home/user/data:/data`.
  * If any of your directory names contain spaces, you should enclose the entire path specification in double quotes. For example: `-v "/home/user/Project Files/data:/data"`
  * If you append `:ro` to the end of the container path, the container will be unable to write any changes to the mapped directory.
  * You can also map a single specific *file* into the container. For example: `-v /home/user/project/config.json:/app/config.json:ro`
  * A tip: Use Bash's `$()` expansion to allow mapping a *relative* path from the current directory. For example, if you are in `/home/user/project` and you want to map `./data` into `/data`, you would use `-v "$(pwd)/data:/data"`.
* `--entrypoint <script_or_program>`: Override the entrypoint script specified when the image was built. This might be useful to debug a container by executing `/bin/bash` as the entrypoint and then exploring the container from inside.
