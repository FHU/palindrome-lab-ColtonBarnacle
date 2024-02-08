def palindrome(word_one):
    if word_one.isspace():
        return 'False'
    elif word_one[0]==word_one[-1] and word_one[1]==word_one[-2] and word_one[2]==word_one[-3]:
        return 'True '
    else:
        return 'False'
        

#YOUR CODE GOES HERE
#run tests LR
word_one = input()
word_one = word_one.replace(" ", "")

print(palindrome(word_one))
