import time

userStr = "" 
userStrLen = 0

# The main part of the calculation and output.

print("Hi! I'll tell you the length of your word, sentence, or even a whole text! (Spaces, punctuation marks, and newlines also count)")
userStr = input()
userStrLen = len(userStr)
print("Its length: " + str(userStrLen) + " characters.")

# Waiting for the program not to terminate immediately.

time.sleep(9999) 