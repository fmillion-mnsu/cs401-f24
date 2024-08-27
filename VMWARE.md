# Installing a Linux virtual machine using VMware products

VMware Workstation (for Windows) and Fusion (for Mac) are professional-grade virtualization software systems that are available for free for educational use. To save you the trouble of signing up for a Broadcom account and all of the fluff that entails, I have provided a link on D2L for you to directly access the installer files. See D2L for the link.

The first section of these instructions will give you the platform-specific instructions for setting up the virtual machine in your environment (Mac or Windows). The second section applies to all users of virtualization, and shows how to install the Ubuntu OS itself into the VM.

## Mac users (VMware Fusion)

VMware Fusion, now free for educational use, supports Apple Silicon processors as well as Intel processors, and (on Apple Silicon) can run virtual machines for both Intel and ARM (Apple) architectures. 

1. Download VMware Fusion from the link on D2L.
2. Install VMware Fusion by opening the disk image and double-clicking the Fusion icon. You will need to enter your password.
3. When asked, choose "I want to license...for personal use".
4. Once you see the main application screen, you're ready to proceed.
   
   If you're on an **Apple Silicon Mac** (most Macs released after mid-2020), download the [latest version of Ubuntu for ARM processors](https://cdimage.ubuntu.com/noble/daily-live/current/noble-desktop-arm64.iso).

   If you're on an **Intel-based Mac** (anything prior to 2020), download the [latest version of Ubuntu for Intel x86-64 processors](https://cdimage.ubuntu.com/noble/daily-live/current/noble-desktop-amd64.iso)

5. Either drag-and-drop the ISO file you downloaded onto VMware, or use the interface to select the downloaded image.
6. Let VMware select the default options for you. It will default to 4GB of RAM and 20GB of drive space - this is plenty for what we will be doing.
7. Once you have finished configuring the VM, the VM will start and you will be launched into the Ubuntu Installer.

Skip to the [Setting up Ubuntu](#setting-up-ubuntu) section.

## Windows users (VMware Workstation)

1. Download VMware Workstation from the link on D2L.
2. Install VMware Workstation by launching the executable file. Work through the installer and select the defaults. You may be asked to restart your computer - do so if sked.
3. Start VMware Workstation. When asked, choose "License...for personal use".
4. You'll now see the main VMware interface. You're ready to proceed.
   
   Download the [latest version of Ubuntu for Intel x86-64 processors](https://cdimage.ubuntu.com/noble/daily-live/current/noble-desktop-amd64.iso)

5. Choose New Virtual Machine under the File menu.
6. Select "Typical" and choose Next.
7. Select the second option "Installer disc image ISO" and then locate the downloaded file on your hard drive.
8. Let VMware select the default options for you. It will default to 4GB of RAM and 20GB of drive space - this is plenty for what we will be doing.
9.  Once you have finished configuring the VM, the VM will start and you will be launched into the Ubuntu installer.

## Setting up Ubuntu

The VM will first show you a text-mode screen with a few options - you want to simply select the default option and let the live CD image boot. 

After a short time you will arrive at the Ubuntu desktop. This is a live CD environment and you can actually "use" Linux at this point. However, this is an *ephemeral* (temporary) environment and nothing you do will be preserved. So we will now install Ubuntu to the drive image you created with the VM.

You should be launched into the Ubuntu Installer automatically - if not, hover over the middle of the screen and choose Ubuntu Installer. 

The installer is very straightforward. You can mostly select the defaults. If you wish to setup as a different root system language you can choose that during the first step if you choose. The rest of the questions will ask about timezone, creating a user account (this is basically the same process that WSL asks about), and what you want to install - again, the defaults are sensible and will work fine for our class.

Once finished, you'll be asked to reboot - go ahead. Note that you are rebooting the *virtual machine*, not your "regular" computer. Once you reboot you can login to your shiny new Linux installation!

> Note that we will spend significant time with the command prompt in this course, so despite a graphical interface being available, you will not use it all that much for our assignments. However, you *can* use the Linux GUI to access D2L or other web resources - you may want to do this so that you're able to copy and paste content into and from D2L as appropriate! (VMware does support clipboard sharing between host and VM, but it requires some additional setup.)