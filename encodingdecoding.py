# Name: Maria Traskowsky
# Section: (C) TU 11:00am - 12:15pm
# Project: Student Grading
# Description: This program uses a dictionary and lists to encode and decode messages based on
# what the user would like to do. If the user chooses to start with the character 'a', 
# then the program will encode or decode the message using the ROT13 cipher. If the
# user chooses to start with a different character, the alphabet will wrap around and the
# cipher will take this into account.

dictionary = { 
    'a' : 1, 'b' : 2, 'c' : 3,'d' : 4,'e' : 5,'f' : 6,'g' : 7,'h' : 8,'i' : 9,'j' : 10,'k' : 11,'l' : 12, 'm' : 13,
    'n' : 14,'o' : 15,'p' : 16,'q' : 17,'r' : 18,'s' : 19,'t' : 20,'u' : 21,'v' : 22,'w' : 23,'x' : 24, 'y' : 25, 'z' : 26,
}
key_list = list(dictionary.keys()) 
val_list = list(dictionary.values()) 

new_val = 1
newer_val = 1
shift = 13
run = 'z'

while run == 'z':
    #ENCODING
    print()
    start = input("Enter the starting character: ")
    ans = input("Encode (e) or decode (d) or quit (q)?: ")
    while ans == 'e':
        response = input("Enter a word: ")
        for letter in response:
            #print(letter)
            for key in dictionary:
                if (letter == key):
                    if (start == 'a'):
                        new_val = (dictionary[letter] + shift)
                    else:
                        new_val = (dictionary[letter] + shift + dictionary[start] - 1)
                    if new_val > 26:
                        newer_val = new_val - 26
                        print(key_list[val_list.index(newer_val)], end = '')
                        ans = 'a'
                    else:
                        print(key_list[val_list.index(new_val)], end = '')
                        ans = 'a'

    #DECODING
    print()
    while ans == 'd':
        response = input("Enter a word: ")
        for letter in response:
            for key in dictionary:
                if (letter == key):
                    if (start == 'a'):
                        new_val = (dictionary[letter] - shift)
                    else:
                        new_val = (dictionary[letter] - shift - dictionary[start] + 1)
                    if new_val < 1:
                        newer_val = new_val + 26
                        print(key_list[val_list.index(newer_val)], end = '')
                        ans = 'a'

                    else:
                        print(key_list[val_list.index(new_val)], end = '')
                        ans = 'a'
    while ans == 'q':
        run = 'v'
        break
        print()