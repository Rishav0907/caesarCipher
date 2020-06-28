import subprocess
import pyfiglet
import random
import sys
subprocess.call('clear')

while True:
    def encryption():
        plainText = input("\nEnter plain text:")

        key = 1
        cryptnum = []
        cipherText=[]
        for i in plainText:
            if ' ' in plainText:
                raise IsADirectoryError("No spaces are allowed")
            if ord(i) in range(97, 123):
                num = ord(i)
                num = num+key
                if(num > 122):
                    extra = num-122
                    num = 97
                    num = num+extra

            if ord(i) in range(65, 91):
                num = ord(i)
                num = num+key
                if(num > 90):
                    extra = num-90
                    num = 65
                    num = num+extra
            cryptnum.append(num)
        print(cryptnum)
        for i in cryptnum:
            cipherText.append(chr(i))
        output=''.join(cipherText)
        print(f"\nCipher Text: {output}", end='')

    def decryption():
        cipherText=input("\nInput the cipher text:")
        Key=1

        plainNum=[]
        for i in cipherText:
            if ord(i) in range(97,123):
                num=ord(i)
                num=num-Key
                if(num<97):
                    lack=97-num
                    num=122
                    num=num-lack
            if ord(i) in range(65,90):
                num=ord(i)
                num=num-Key
                if(num<65):
                    lack=65-num
                    num=90
                    num=num-lack
            plainNum.append(num)
        for i in plainNum:
            text=chr(i)
            print(text,end='')
    def main():
        banner=pyfiglet.figlet_format("Caesar Cipher")
        print(banner)
        print("Choose one of the following options")
        print("=====================================")
        print("1. Caesar Cipher Encryption")
        print("2. Caesar Cipher Decryption")
        print("3. Exit")
        option=int(input("\nEnter your choice:"))
        if option==1:
            encryption()
        elif option==2:
            decryption()
        elif option==3:
            sys.exit()
        else:
            raise KeyError("Option not found")
    main()
