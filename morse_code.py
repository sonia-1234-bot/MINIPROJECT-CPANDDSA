import pygame
import time

pygame.init()

pygame.mixer.init()
def code_sound(dot_dash):
    for j in dot_dash:
        if j==".":
            print(".",end="")
            sound=pygame.mixer.Sound("ping-82822.mp3")
            sound.play()
            time.sleep(1)
        elif j=="-":
            print("-",end="")
            sound1=pygame.mixer.Sound("beep-1-sec-6162.mp3")
            sound1.play()  
            time.sleep(1)  
    print(end=" ")    

morse_code={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."}

def find_key(val):
    for key,value in morse_code.items():
        if value==val:
            return key

while True:
    choice=int(input('''Type 1 to convet Text to Morse Code
Type 2 to convert Morse Code to Text
Type 3 to exit 
'''))

    if choice==1:
        text1=input("Enter the text you want to convert: ")
        text=text1.upper()
        print(f"{text1} in Morse code is: ",end=" ")
        for k in text:
            #print(morse_code.get(i),end=" ")
            code_sound(morse_code.get(k))
        print()    
    elif choice==2:
        morse=input("Enter the morse code with space for letter: ")
        print(f"{morse} in letter is: ",end=" ")
        m=morse.split(' ')    
        for i in m:
            print(find_key(i),end="")
        print()      
    elif choice==3:
        exit()
    else: 
        print("Invalid choice!!!")            
