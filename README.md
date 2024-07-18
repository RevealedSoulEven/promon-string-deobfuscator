# Promon Shield String Deobfuscator

This project is used to decrypt dex strings for Promon Shield protected-apps.

✨<b>[NEW] Now it can decrypt</b> the strings which are passed to the functions at runtime (dynamically) but almost every string in dex is getting decrypted.

<i>Still, it can't decrypt the strings which are being decrypted by functions of different classes coz, it needs to save each and every function and its very hectic to store all functions. I'll try to add this feature soon in the next update.</i>

Working is quite simple, just reading the smali patterns and opcodes (which I added) and then decrypts them using some logic.
I request contributors to please add new features. Thank you in advance. ILY <3

## Why?

Just because I couldn't bypass Frida detection because I'm a noob, so I did this.

## Credits

- Me

## Installation

Get the smali folder using [Smali](https://github.com/JesusFreke/smali) and then open the Python script and add the name of the folder at the end of the script. 
Save and RUN!

Happy Reversing 😉
