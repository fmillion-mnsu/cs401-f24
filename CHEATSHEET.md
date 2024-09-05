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
