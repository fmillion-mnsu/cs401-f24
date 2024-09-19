# Using VS Code in Linux

This document explains how to install [Visual Studio Code](https://code.visualstudio.com/) so that you can use it to edit your Bash scripts.

## Windows (WSL)

If you are using WSL and have VS Code installed on your Windows machine, you are already all set. Just type `code <filename>` in a Bash shell (replacing `<filename>` with the file you want to edit) and VS Code will open on your Windows machine. You can also pass a directory name to open the whole directory in VS Code.

## Virtual Machine (VMware on Windows or Mac)

1. Visit the [VS Code Download Page](https://code.visualstudio.com/download) in a browser on your Linux system.

1. Download the `.deb` version of the installer from the middle column. 

    * If you're on a Windows PC using VMware Workstation, or you're using VMware Fusion on an Intel Mac, download the **x64** version.
    * If you're on an Apple Silicon Mac using VMware Fusion, download the **Arm64** version.

1. In Bash, switch into your `Downloads` directory.

1. Run this command:

        sudo apt install ./code*.deb

    This will install VS Code.

1. Run VS Code. It should finish the configuration for you.

You should now be able to use `code` at the command prompt to open scripts or directories in VS Code on Linux.
