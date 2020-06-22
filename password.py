import string
import random
s1=string.ascii_lowercase                #s1=abcdefghijklmnopqrstuvwxyz
s2=string.ascii_uppercase                #s2=ABCDEFGHIJKLNMOPQRSTUVWXYZ
s3=string.digits                         #s3=0123456789
s4=string.punctuation                    #s4=./';"]}{[-*/ .....etc
len1=int(input("Enter password length:"))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
"""
s=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#',
'$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']',
'^', '_', '`', '{', '|', '}', '~']
"""
print("Your Password: ", "".join(random.sample(s,len1)))