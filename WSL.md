# Installing Linux on Windows systems using WSL

This process is quite straightforward and requires only a few steps.

> Caveats:
>
> * If you are using a virtualization system for another class, such as VMware Workstation or VirtualBox, those programs may or may not need some configuration changes after installing WSL. In particular, WSL enables the Windows Hypervisor platform; other virtualization programs must then use the HVP rather than their own engine. This should be automatic, but if you have trouble you can ask me for help.
> * Installing WSL won't take much room, but there are some potential issues with growing disk space usage. A process known as *compacting* can be used to recover disk space if the WSL image gets too large. See later in this document for details.

1. Bring up the Run dialog box by pressing Windows+R. Enter `cmd` into the box, then press **Ctrl+Shift+Enter**.

   > As an alternative, you can look for Command Prompt in your Start menu, and then hold down **Ctrl** and **Shift** while clicking on it.

2. Approve the authentication request.

3. Type `wsl --set-default-version 2` and press Enter. This command sets WSL to use the new WSL 2 by default. You need this for our class. (It's also required for tools like Docker.)

4. Type `wsl --install ubuntu` and press Enter. The process will take some time to install and configure WSL. If you haven't already used WSL on the system, you may need to reboot.

5. After WSL installation completes, you'll be prompted for a UNIX username. This can be, but *does not need to be*, the same as your normal PC username. Remember what this username is.

6. You'll then be asked for a password. This is the password you will use under Linux to get administrative (root) access. Make sure you make note of the password! If you forget it, you either must do some advanced administrative steps to revert/reset the password, or you must completely erase your WSL instance and start over.

7. You'll finally be dropped to a Linux prompt - it ends with a `$`. Congratulations! Type `exit` to close WSL.

You're now all set. WSL should have added a profile for you under Windows Terminal if you have it. Otherwise you can always get to a WSL prompt by looking for Ubuntu in your Start menu.

## Compacting

TODO: write this
