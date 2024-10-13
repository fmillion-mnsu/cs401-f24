# Individual Assignment #2

This is an **individual** assignment for this course. Each class member will submit their *own* work - you may assist each other but you may *not* share or receive code with/from others.

## Task

This exercise will give you a chance to explore Bash scripting in detail.

Choose **any three** of the following script options and write the script using the tools and techniques you've learned. You may use Bash as well as any generally available command line tool (such as `ls`, `cat`, etc.) in your script. You may also use helper scripts and `source` to organize functions and code.

### Option 1: File organizer

Write a Bash script that implements the following:

* Accepts a directory as a parameter. If not given, assume the current directory. (Hint: you can either use `pwd` to get the directory, or just use `.`)
* Within the given directory, iterate over each file. Create a directory for the file's extension and move the file into it.
  * Useful hint: `mkdir -p` will make a directory but not produce an error if it exists already
* Files with no extension *should not* be moved.
* When done, print the *total* number of files moved.

### Option 2: Replace string in files

Write a Bash script that implements the following:

* Accepts a minimum of three parameters. The first is a string to search for, the second is a replacement string, and the third (and subsequent!) parameters are filenames.
* Not providing enough parameters should print an error and exit with a nonzero exit code (e.g. `exit 1`)
* Use `getopts` to accept a `-n` parameter that will **print** matching lines (with replacements made) on screen but **not** write any files to disk.
* Make a directory called `replacements`.
* For each file, open the file and read it line by line. Use parameter expansion to replace the search string with the replacement string.
  * Hint: you can use `echo` along with `>>` to append strings to your output files.
* Print the **number of times** a replacement was made.

### Option 3: Statistical Line Counter

Write a Bash script that implements the following:

* Accept a single filename as a parameter. Not specifying a filename means the script should **read from standard input**.
  * Hint: use a `while` loop with `read` to read lines. If a filename was given, use `<` after the `done` in your `while` loop to read from a file rather than standard input.
* For each line, get the **length** of the line and increment a value by one, indicating that a line with that length was found.
  * Hint: `${#VARIABLE}` gives you the length of the string in `VARIABLE`.
* At the end, print a list of all lengths. You don't need to sort by occurrence; simply printing an incrementing report is fine. Do **NOT** include lengths that had zero occurrences.

Example output might look like:

    Length   Count
    ------   -----
    5        4
    13       2
    33       3
    34       1
    45       5

### Option 4: Random Number Generator

`$RANDOM` is a special variable that will always return a random integer between `0` and `32767`.

Write a Bash script that implements the following:

* Accepts one positional parameter, which is a filename. If a filename is not given, output generated should be printed to standard output.
* Use `getopts` with a parameterized option (your choice what letter) to accept a count of numbers to generate. **If no value is given by the user in this way, assume 100 numbers should be generated.**
* Use the special `RANDOM` variable to generate as many random numbers as was requested. Either print the random numbers on standard output, or write them to the file if it was given.
* Keep a **running total** of the numbers generated.
* The last line of the output should be the **total** of the generated numbers.
* Use a **function** to actually generate and print the random number. Call your function each time you need to use it.

### Option 5: Classic Logic Game

Write a Bash script that implements the following:

* No parameters needed. If they are provided they can be ignored without error.
* A 5-digit random number is chosen. 
  * Hint: This operation will give you a random number between 10000 and 99999: `$(((RANDOM * 32768 + RANDOM) % 90000 + 10000))`
* The user should be given 10 guesses. For each guess:
  * The user inputs a 5-digit guess.
  * The program will determine how many numbers the user guessed are in the **correct place**, and how many numbers are **in the number, but not in the correct place**.
  * Example: if the number to be guessed is `12345` and the user enters `52396`, the game should indicate that 2 numbers are in the correct place, and 1 number is in the digits but is not in the correct place.
* If the user guesses the number within 10 tries, indicate that the user won. If not, print the correct answer and tell the user they lost.
* Print basic instructions for the game each time it starts!

## Requirements

* It is up to you to generate **test data** for scripts that need input data. How you do this is up to you - you can copy text from outside sources, generate data manually, write a program in a language of your choice to generate the data, write a Bash script to generate data (!), etc. Include test data you generate with your submission if applicable.
* Your scripts **must** end with the `.sh` extension. You may, however, name your script anything you like (within reason - don't make me deal with escaping colons or forward slashes please!)
* Remember to include the *shebang* string at the top of all scripts! (`#!/bin/bash`)
* Remember to make the script executable before testing.

## Submission

Use `tar` to create a **tar archive** of your scripts and any supporting files. Submitting individual scripts will result in some point loss! (You can make a `.tar.gz` or other compressed version if you wish.)

This assignment is due **Wednesday, October 2nd** at **11:59 PM**. 

## Grading

The following are the requirements for your submission:

* Submitted in a `.tar` (or compressed `tar`) file
* All scripts run without error (unless an error should be generated, e.g. user didn't provide required parameters)
* Scripts accomplish the tasks given in the descriptions
* Test data included that you used for development/testing
