"""
Program name : Task 3 for controlled assement
Programmer : Finn
Date of last edit : 22/01/16
Notes : Had problem with program not encrypting.Fixed on 22/01/16

"""

def menu():
    #try:
    alphabet = ("abcdefghijklmnopqrstuvwxyz1234567890!#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
    encdec = input("Would you like to \n\
1.encrypt input (1)\n\
2.decrypt input (2)\n\
3.encrypt file (3)\n\
4.decrypt file (4)")
    if encdec == '1':
        encode(alphabet)
    elif encdec == '2':
        decode(alphabet)
    elif encdec == '3':
        encodeff(alphabet)
    elif encdec == '4':
        decodeff(alphabet)    
    else:
        print("You inputted an incorrect value to one of the variables.\n\
Please try again")
        menu()
    #This catches everything
    #except:
        #print("Wow thats some strange data")
        #menu()
        
        
def encode(alphabet):
    #changed this from " " to "" meaning it removes space
    word = input("What word would you like to input? ").lower().replace(" ","")
    wordlen = len(word)
    #same here
    codeword = input("What is your codeword? ").lower().replace(" ","")
    codelen = len(codeword)
    newcodelen = int(wordlen/codelen)
    extra = wordlen % codelen
    fullkey = ""
    for i in range(0,newcodelen):
        fullkey=(fullkey+codeword)
    trimmedkey = codeword[0:extra]
    fullkey = fullkey + trimmedkey
    encoded = ""
    for i in range (0,wordlen):
        offset = alphabet.find(fullkey[i])
        enc = alphabet.find(word[i])
        finalposition = (offset + enc) % 67
        nextletter = alphabet[finalposition]
        encoded = encoded + nextletter
    print("Your encoded message is " + encoded)

def decode(alphabet):
    word = input("What code would you like to decode? ")
    wordlen = len(word)
    codeword = input("What is your codeword? ").lower().replace(" ","`")
    codelen = len(codeword)
    newcodelen = int(wordlen/codelen)
    extra = wordlen % codelen
    fullkey = ""
    for i in range(0,newcodelen):
        fullkey=(fullkey+codeword)
    trimmedkey = codeword[0:extra]
    fullkey = fullkey + trimmedkey
    decoded = ""
    for i in range (0,wordlen):
        offset = alphabet.find(fullkey[i])
        enc = alphabet.find(word[i])
        finalposition = (enc - offset) % 67
        nextletter = alphabet[finalposition]
        decoded = decoded + nextletter
    decoded = decoded.replace("`"," ")
    print("Your decoded message is " + decoded)

def encodeff(alphabet):
#function name encodeff, short for encode from file
    fullkey = ""
    final = ""
    filename = input("What is the text file directory of the text you wish to encode? \n\
An example of this would be 'D:\codnig files\finn \n")
    file = (filename+".txt")
    file2 = (filename+"2.txt")
    fg = open(file2,mode="w")
    fg.close()
    f = open(file,mode="r")
    count = len(open(file).readlines(  ))
    key = input("What key do you want? ")
    f = open(file,'r')
    for line in f.read().split('\n'):
        for d in range(0,len(line)):
            temp = alphabet.find(line[d])
            temp2 = alphabet.find(key[(d%len(key))])
            temp3 = temp + temp2
            temp4 = temp3 % 67
            final = final + alphabet[temp4]
        final = final + "\n"
        f = open(file2,mode="a")
        f.write(final)
        final = ""
    f.close()

    
def decodeff(alphabet):
#function named decodeff short for decode from file
    print("")






while 1:
    menu()
