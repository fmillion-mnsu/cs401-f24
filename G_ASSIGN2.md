# Group Assignment 2

In this assignment, you will build a "system information tool" by using only the various files and directories offered as part of Linux's "pseudo-filesystems".

You may code this tool in any language of your choosing, including Bash script, Python, Java, C# .NET, and so on. All of these can be used to develop for Linux - it's left as an exercise to your group to figure out how to install any necessary tooling and support packages. Please refer to [Using VS Code in Linux](VSCODE.md) for info on how you can use VS Code as your editor both on native Linux in a VM as well as on WSL. Other editors *may* offer WSL support but this is not guaranteed; it's also possible to install many (but not all) editors on Linux natively if you're using a virtual machine.

This exercise will involve reading files and directories and parsing their contents. You should not need any especially advanced text processing skills to accomplish the tasks in this assignment, but some knowledge of methods such as regular expressions may prove useful. You can perform all of the text processing required by using simple operation such as substrings, string split, etc. 

## Requirements

Write a command line tool that obtains and prints all of the following information about the current system. Details about each piece of info and where you can obtain it are indicated below.

* The name of the CPU in the system. (`/proc/cpuinfo`, listed under `model name`, you can grab the name of the first CPU instance)
* How many CPU cores are in the system. (`/proc/cpuinfo`, just count how many info blocks are present)
* How many GB of RAM are in the system. (`/proc/meminfo`, the `MemTotal` line shows the RAM in KB, convert it to GB for output.)
* How many GB of *available* memory exists (`/proc/cpuinfo`, the `MemAvailable` line. Hint: Don't use `MemFree`, this actually means something completely different!)
* A list of all storage devices in the system, excluding "loop" devices and RAM disks. (each block device is listed as a directory in `/sys/block`. Exclude any device starting with `loop` or `ram`)
  * For **each** block device, also print the total size in GB of the device. (Within each directory under `/sys/block` is a file called `size`, which reports the size of that disk in **512 byte sectors**. You will need to figure out the math to print the size of the disk in GB.)
* The device identifier for the root filesystem. (`/proc/mounts` contains a list of all mounted filesystems. The first column is the device ID, the second is the mount path - look for which entry has its mount path as simply `/`.)
* How many filesystems in total are mounted. (Just count the lines in `/proc/mounts`)
* How many processes are running on the system. (Count how many directories are names consisting of just digits in `/proc`)
* The command line that has been supplied to the currently booted kernel. (`/proc/cmdline`)
* The version ID of the currently booted kernel. (`/proc/version` contains a string with several tokens - the current version ID is the third token (#2 if counting from 0).)
* How long the system has been booted, in **hours, minutes and seconds**. (In `/proc/uptime` you'll find two values - the first is the number of seconds since the system booted.)

## Deliverable

Simply upload your completed source code for your script to D2L.

This is a **group** project - only **one** submission per group is required.

The due date for this assignment is **Wednesday, October 9** at **11:59 PM**.

## Resources

This assignment only scratches the surface of the breadth of information available via simple interfaces such as the files in `/proc` and `/sys`. You can install the package `lshw` if you want to try a very comprehensive system information tool that extracts a large amount of information via these interfaces. 

Also note that nearly every other tool that presents information about your system is using these interfaces to obtain that information. Commands such as `free`, `top`/`htop`, `uptime`, `uname` and so on are all simply accessing the data provided by these virtual files!
