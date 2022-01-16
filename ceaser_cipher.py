#python script to encrypt string with ceaser cipher
import string
import re
from unittest import case


def caeser_cipher(str, shift = 10):
#creates a dictionary where a=1, b=2 etc 
    conv_table = dict.fromkeys(list(string.ascii_lowercase),"")
    value = 1
    for k in conv_table: 
        conv_table[k] = value; value += 1  

#creates an alst of the alphabet
    letter_array = string.ascii_lowercase

#turns string in list but keeps casing
    case_array = list(str)

#turns str into downcase list
    str_array = list(str.lower())

#turns string into an array of numbers
    num_array = []
    for l in str_array:
        if re.match("[a-z]",l):
            num_array.append(conv_table[l])
        else:
            num_array.append(l)

#shifts number by argument
    alt_array = []
    for num in num_array:
        if isinstance(num,int):
            alt_array.append(num + shift)
        else:
            alt_array.append(num)

    #creates output array of shifted letters
    output_array = []
    for num in alt_array:
        if isinstance(num,int) != 1:
            output_array.append(num)
        elif num <= 26:
            output_array.append(letter_array[num-1])
        else:
            output_array.append(letter_array[num - 27])


#checks is any characters in letter_array where upcase and creates an array with uppercase letters =1 and lower case =0
    upcase_array = []

    for let in case_array:
        if let.isupper():
            upcase_array.append(1)
        else:
            upcase_array.append(0) 


#create new array with captilisation added back in
    case_output_array = []
    for index,value in enumerate(output_array):
        if upcase_array[index] == 1:
            case_output_array.append(output_array[index].upper())
        else:
            case_output_array.append(output_array[index])


#join array into a string. Checks the shifting is not >26 each end of the alphabet
    caeser_string = "".join(case_output_array)
    if shift > 26 or shift < -26:
        print("Shift too large, or too small!")
    else:
        print(caeser_string)


caeser_cipher("what  string!",5)
