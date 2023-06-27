# Inputs
import string
# https://docs.python.org/2/library/string.html#
# https://www.youtube.com/watch?v=JEsUlx0Ps9k - video

alphabet = (string.ascii_lowercase, string.ascii_uppercase)
# https://www.youtube.com/watch?v=qjPYBtawBLM - video

text = input("Please enter a password (length is unlimtied and only contain letters) >>")
while len(text) == 1 and text.isnumeric() and text.isalpha():
    text = input("type a vaild password >>")
shift = 3
encryptword = ""

# Nevaeh
# I used import string to help with some of the constants such as lower.case and upper.case.
# I made my inputs for how many shifts to the right the program should go
# Since we are using the program as someone inputing the message, I put encryptword = "" for the progam to show whatever the person entered as the message to be encrptyed


# Encrypting
for message in text:
    i = ord(message)
    i += shift
    encryptword += chr(i)
print(encryptword)
# https://www.pythonpool.com/caesar-cipher-python/ - article
# https://www.youtube.com/watch?v=deuhkYSaHaQ


# Nevaeh
# For the Encrypting, I was having a hard time doing an if or else funcation. I wanted to find a simple way and I found this from a video linked below
# However, I changed varibles and did not add the ord numbers like it was in the video and Natasha put the text.isalpha with the while len()
# Since we were using input a word or message, I did not have character as the variable since it was not one word we were encrypting by itself
# The i that I put next to chr for character, shift, and ord was there to represent the characters of the message as varibale.
# I changed it from an X to i, becuase i was just used to seeing an i in python. It doesn't change much of the outcome, it was jsut something for me
# The i = ord(message)
# the i += shift is there to tell the program to shift the alphabet 3 times, which was the input I gave it at the top.
# So all the characters that were given in the message will be shifted to another letter 3 to the right.
# encrptword += chr(i) is telling the program to encrypt the characters, which are the varibles i.
# then I printed the encrptyword
# For the encrptyion, you might see at the bottom I found out the ord.
# the ord needs to know what the values are from A through Z to not go over the value of Z
# I did that with print(ord("")) with both a and z to find the numbers.
# At first I was using thr AscII table to find the ord, but I was confused so I found a video that made it easier for me to find them.
# however, I found the program worked without the ord being put into the for message. and because I changed the function from if, else, to a loop
# I did turn the ord into a comment so they would not affect the output

# Nevaeh
# Finding ord
# print(ord("a"))
# print(ord("z"))
# https://www.youtube.com/watch?v=deuhkYSaHaQ


# Decrypting
decryptword = ""
for alphabet in text:
    i = ord(alphabet)
    decryptword += chr(i)

# print(text.translate(encryptword)
print(decryptword)

# Nevaeh
# I did mention the text.translate and we did try to use it.
# It worked but the program was translating the word for each later on by one while giving up the final decrpyted word
# we deicied to just use print(decryptword) instead.
# link to the document with more resources = https://docs.google.com/document/d/1Cv3vXeWG5anMlKUKXUtEoKQNjIjM7Ltkrh4VlQdH2eg/edit