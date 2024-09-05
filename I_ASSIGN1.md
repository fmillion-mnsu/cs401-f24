# Individual Assignment #1

This is your first **individual** assignment for this course. Each class member will submit their *own* work - you may assist each other but you may *not* share or receive code with/from others.

## Preparation

If you haven't done so already, **install** the `hxtools` package into your Linux environment.

> As a refresher, on Debian-based systems, you use the `apt` package management tool to install packages.
>
> Since you must be `root` to install new software, you can use the `sudo` command to run `apt` to install the package like this:
>
>     sudo apt update
>     sudo apt install hxtools
>
> You will need one of the programs installed by `hxtools` for this exercise.

## Task

This exercise will give you practice writing simple shell scripts that read input and produce output via **pipes**.

Write a script that does the following:

1. Read one *entire line* of text from the input - either from the user typing or from the user *piping* a file to the input
2. Convert the string to the `rot13` version of the string using the `rot13` tool.

   > Remember that `rot13`, like many Linux/UNIX utilities, is a sort of "building block" that you can use in assembling operations. It accepts input on its *standard input* stream and produces output on its *standard output*.

   > **Hint**: There are a few ways you can accomplish this task. Essentially, your goal is to end up with a *variable* containing the *result* of the `rot13` operation.

3. Use the `sha1sum` command to compute the cryptographic SHA-1 hash of the string you ran through `rot13`. Capture this value into a variable as well.
4. Print the following output on three separate lines:

    * The original string the user input
    * The result of the `rot13` operation
    * The result of computing the SHA-1 hash of the `rot13` processed string.

**Test your script** with the following input and expected outputs:

> Input: hello world
> rot13: uryyb jbeyq
> sha1sum output: 50ed859a45464b63e1a95cba5b30105637ef55d5

> **Important**: Remember to use `chmod u+x` on your script file before running it to make it executable.

> **Important**: Execute your script using `./script_name.sh` (replacing `script_name` with whatever you named your script). Remember that this is because Bash does not look in the current diretcory for executables; you need to explicitly give the path as the current directory (`.`) to make it do so.

## Requirements

* Your script file must end with the `.sh` extension. You may, however, name your script anything you like (within reason - don't make me deal with escaping colons or forward slashes please!)
* Your script *may* print a prompt for user input if you desire, but it is not required.
* The script *must* be able to accept input via piping. For example: `echo hello | ./script.sh`
* Remember to include the *shebang* string! (`#!/bin/bash`)
* Remember to make the script executable before testing.

## Submission

This assignment is due **Monday, September 9th** at **11:59 PM**. 

It is possible that D2L may not allow you to submit a shell script file. In that case, use the following command to create a *zip file* containing your script and submit that:

    zip -9 submission.zip <your-script-file>.sh

This will create a file `submission.zip` that you can then upload to D2L. You may name the zip file something else if you choose, but please make it sensible.
