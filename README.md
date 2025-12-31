# Promon Shield String Deobfuscator ( string.intern() )

This project is used to decrypt dex strings for Promon Shield protected-apps.
Making the apps easier for static analysis.

✨<b>[NEW] More Speed.</b> Optimised the code for 10X+ performance speed.

✨<b>[NEW] Now it can decrypt</b> the strings which are passed to the functions at runtime (dynamically) and almost every string in dex is getting decrypted.



Working is quite simple, just reading the smali patterns and opcodes (which I added) and then decrypts them using some logic.
I request contributors to please add new features. Thank you in advance. ILY <3

## Why?

Just because I couldn't bypass Frida detection because I'm a noob, so I did this.

## Credits

- Me

## Installation

Get the smali folder using [Smali](https://bitbucket.org/JesusFreke/smali/downloads/smali-2.5.2.jar) ([source](https://github.com/JesusFreke/smali)) and then open the Python script and add the name of the folder at the end of the script.
Save and RUN !!!
Use a single classes.dex at a time.
After deobfuscation is completed, use [Baksmali](https://bitbucket.org/JesusFreke/smali/downloads/baksmali-2.5.0.jar) ([source](https://github.com/JesusFreke/smali)) and convert the smali folders back to classes.dex

Happy Reversing 😉
