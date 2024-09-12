# Group Assignment

For this assignment, you'll be building your own kernel!

If you're using VMware, you can actually try booting your kernel as well. It is possible to boot a different kernel on WSL but it can be a bit challenging since the WSL kernel has special requirements (for example, a driver that allows Linux direct access to your Windows files). 

> Building the kernel is quite processor-intensive. You should work together in a group, but I suggest you determine who has the most powerful machine in your group and use that machine for the process.

## Steps

1. Ensure that you have all of the tools necessary on your Linux installation to build software. On Ubuntu, the following command will install the **toolchain** used for compiling C and C++ applications, including the kernel: `sudo apt install build-essential`

2. In your Linux environment, get the current **stable** kernel source code from <https://www.kernel.org/>. The current version as of this writing is [6.10.9](https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.10.9.tar.xz).

3. Use `tar` to **extract** the source code. Refer to the cheatsheet or the slides from September 12th.

   If you kept the source tarfile in your downloads folder, it'll create a directory of the same name as the tarfile. Note that this is because the files in the tarfile are stored with a path that includes the Linux kernel version as a directory. This is NOT always the case!

   Once the extraction has finished `cd` into the newly extracted directory.

4. We'll start by essentially replicating the configuration of the kernel that you are already running. Even though your Linux installation is probably using an older kernel, this is OK since the configuration system will automatically apply sensible defaults for any new options.

   There should be a file on your system called `/proc/config.gz`. (We'll be talking about the `/proc` filesystem later.) Use the `cp` command to copy this file into the source tree.

5. Decompress the `config.gz` file using `gzip`: gzip -d config.gz

   This will yield a file simply named `config`.

6. Rename the file called `config` to `.config`. (Yes, it starts with a period - recall that this means the file is hidden.) We do this so that the config file won't get accidentally copied if you were to clone the source tree for whatever reason. 

   `mv config .config`

7. Since we're trying to replicate your existing kernel, we will not yet make any configuration changes. However, we do need to update the `.config` file to reflect any new options that might have been added since your running kernel was built:

   `make olddefconfig`

8. Finally, build the kernel!

   * On Intel PC (VMware or WSL): `make -j$(nproc)`
   * On Apple Silicon Mac: `make ARCH=arm64 -j$(nproc) Image`

   This command creates a `bzip2` compressed kernel executable image. 

   The `-j$(nproc)` parameter adds the `-j` option, followed by the return of the `nproc` command. The `nproc` command simply returns a value indicating the number of CPU cores your system (or virtual machine) has available. (Recall that the `$( )` syntax expands to the value printed by the command inside the parentheses!) The `-j` option specifies to the `make` command how many CPU cores it should use for compilation - this will allow for multi-core compiling, which will be much faster than traditional single-core compilation.

   Note that building the kernel can take some time. On a decently powerful laptop, it will probably take at least 30 minutes. During the compile, you'll see the name of each source code file that is being built scrolling up your screen. Your PC is very busy while this is happening!! As long as you still see filenames scrolling and no error, your kernel build is still proceeding. You may want to take a break while it builds!

9. If all went well, the compiled kernel will be located at:
    * Intel: `arch/x86_64/boot/Image`
    * Apple Silicon: `arch/arm64/boot/Image`

You can do `ls arch/x86_64/boot` or `ls arch/arm64/boot` to list the directory and see if the `Image` file was created.

   If so, congratulations - you built a kernel!

   Create a project directory, such as in your home directory (e.g. `/home/your_username/assignment1`). **Copy** the `Image` file out of the above path into the directory you created. After copying, rename the `Image` file to `Image1`. I leave it as an exercise to you to create a directory and copy and rename the `Image` file there.

   > Note that the kernel actually doesn't contain many drivers internally. Most modern Linux setups use **loadable modules** for drivers, which are essentially pieces of code that can be injected into the kernel at runtime.
   >
   > Building the kernel *does* build the modules, so the build still takes quite some time.

10. Now, we're going to make a modification to the kernel.
  
    Run `make nconfig`.

    This will open up a full-screen menu interface in which you can configure the kernel. Explore the many options you have available - this will give you an idea of what sorts of functions the kernel does. (It's a *lot*.)

    You'll find sections for networking (both hardware drivers as well as software routing, firewalls, etc.), storage hardware, filesystems (NTFS, FAT, etc.), cryptographic algorithms, and much more. All of these functions are compiled into your kernel, or are compiled as modules. An `M` in a configuration option means that option will be compiled as a module rather than built into the kernel image itself.

    In most cases you can press `H` while an option is selected to get a screen of help information about that option.

    > There are many reasons you might want to use modules other than for size optimization. Loading a kernel module at runtime means you can programmatically configure the module after the system has booted. Otherwise, you have to know the values for the configuration prior to the system even booting, which may not even be possible.

    > Custom kernels, such as those modified by device manufacturers, will likely have additional options that aren't available in this **mainline** kernel. Additionally, kernel patches are often made available to add hardware support for devices that aren't included in the kernel itself; those patches will usually add options to this configuration interface for building the feature into the kernel.

11. Under `General Setup`, arrow down to `Local version` and press Enter.

    In the box that appears, **add a hyphen, followed by each of your group member's first names separated by hyphens**. For example `-flint-rushit-mansi-ryne`.

    You should see the text you entered appear in the menu entry.

12. Exit the configuration interface.

13. Build your new kernel again using the command in step 8.
   
    Since we already built the kernel before, the rebuild will be much faster!

    You can verify if your kernel built successfully with this command: `file arch/x86_64/boot/Image` or `file arch/arm64/boot/Image`

    If you successfully built your newly modified kernel, you should see something like this:

    `arch/x86_64/boot/Image: Linux kernel x86 boot executable bzImage, version 6.10.0-flint-rushit-mansi-ryne (root@localhost) #1 ...`

    If you see your group member's names in there, you've successfully built a *custom* kernel!

14. Copy your *custom* kernel to the directory you created in step 9, and **rename** the image file to `Image2`.

    > If you renamed the first kernel image file from `Image` to `Image1`, copying the new `Image` file into your output directory won't overwrite the original build. However, if you did *not* rename the file first, copying the new image will *overwrite* the original. Your submission must contain *both* kernel images!

15. The final step for building most kernels is to build and copy the **modules**.

    Run this command to finish building and copy the module files to your output directory:

    * Intel: `make INSTALL_MOD_PATH=/home/<...path to your project dir...>/modules modules_install`
    * Apple Silicon: `make ARCH=arm64 INSTALL_MOD_PATH=/home/<...path to your project dir...>/modules modules_install`
   
16. To submit your assignment, switch into your project directory and use the `tar` command to make an **archive** of the directory. Use the `-j` command line option to use bzip2 compression. 

    Name the file `group1-kernel.tar.bz2`.

    For example, after switching into your project directory:

    `tar -c -j -f group1-kernel.tar.bz2 .`

    > The `.` indicates to compress the current directory. `tar` will indicate a warning that it can't compress the file it's currently writing the archive to - that is OK.

    Finally, submit this file on D2L.

    > If you are having trouble sending the file on D2L because of its size, you may also place the file in your OneDrive and create a Share link that gives me access to download it. You can post that OneDrive link as your submission on D2L. If you need help on this please contact me.

Good luck!
