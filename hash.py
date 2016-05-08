#!/usr/bin/env python2.7
#author:Nancy Lalluwadia
#date:7/5/2016
#About Program:Here is a code to find a 9 letter string of characters that contains only letters from :acdegilmnoprstuw
#such that the hash(the_string) is: 930846109532517
# hash is defined by the following code:

reserved_letters = 'acdegilmnoprstuw'
letters_tobe_reversed = 'leepadg'

#For example, if we were trying to find the hascode for  string 'leepadg' as per below function it will be --> 680131659347 .
def hashCode(string):
    '''generate hash code from given string s'''
    h = 7
    reserved_letters = "acdegilmnoprstuw"
    for i,v in enumerate(string):
        h = (h * 37 + reserved_letters.index(v))
    return h


hash_value = hashCode(letters_tobe_reversed)
#hash_value code will be 680131659347

#For example, if we were trying to find the 7 letter string where hash(680131659347) answered string is-->  "leepadg".
def deHashCode(hash_code):
    '''reverse back the string value from the given hash code'''
    rm = hash_code % 37
    hash_code = (hash_code-rm)/37
    if (hash_code == 7):
        return reserved_letters[rm]
    return deHashCode(hash_code) + reserved_letters[rm]
	
print("Reverse hash string value of hash code 930846109532517 is: "+deHashCode(930846109532517))
print("\nReverse hash value of hash code 680131659347 is: "+deHashCode(hash_value))
