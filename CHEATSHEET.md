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

### Getting system information

* `lscpu`: Show information about your CPU
* `free`: Show overall memory information
* `df`: Show disk usage and free space
* `lsblk`: List all **block devices** in the system

## `nano` Editor

* `Ctrl+X`: exit Nano. It will ask you to save the file if it has been changed.
* `Ctrl+K`: delete the current line and put it on the clipboard. (If pressed repeatedly, copies each additional line to the clipboard. If you change location however, the clipboard is cleared before copying.)
* `Ctrl+U`: Paste the clipboard contents
* `Ctrl+F`: Search in file
* `Ctrl+O`: Save current file without exiting Nano
* `Right Alt (Meta) + U`: Undo command

## Bash Scripting

### Piping

* Take output of one command and send it to input of next command: `|` (shift+backslash) Also known as the pipe character or "vertical bar"
* Write the output of the final command in a chain to a file, **overwriting** the file if it exists: `>`
* Write the output of the final command to a file, appending to the file if it exists: `>>`
* Send the contents of a file to standard input of the first command in a chain: `<`

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

#### Internal variables

These variables are defined by Bash and are available in scripts:

* Positional variables `$1`, `$2`, ...: Contains values passed either into the script on the command line or into a function
* `$#`: Contains the number of parameters passed to the script or function
* `$*`: Contains all parameters as a single, non-iterable string
* `$@`: Contains all parameters in an iterable string, split by space (or by `$IFS`)
* `$?`: Contains an integer representing the return value of the last executed command
* `$IFS`: Contains the character used to split the parameters to functions. Defaults to a space. Can be set to change the separator prior to e.g. calling a function

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
