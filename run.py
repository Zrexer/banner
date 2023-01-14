import pyfiglet


text = " " # Your Name  

print('\033[31m' + pyfiglet.figlet_format(text, font='slant') + "\n" + '\033[34m' + "_" * 49 + '\033[00m')
