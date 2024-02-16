alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import arts
print(arts.logo)
def caesar(text,shift,direction):
    end_text = ""
    if(direction=="decode"):
            shift*=-1;
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            new_position=new_position%26;
            end_text+=alphabet[new_position] 
        else:
                end_text+=char;
        
    print(f"The {direction}d result is {end_text}")

flag=True
while(flag==True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))   
    caesar(text,shift,direction)
    choice=input("Do you want to use the Cipher again?? [yes or no]")
    if(choice=="yes"):
         flag=True
    else:
         flag=False

    
