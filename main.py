word=input("Please enter a word/letter/phrase. ")
word=word.lower()
#This line checks user input and checks if the given phrase/word is a palindrome. It does this by taking a string, trimming it, and running the functions recursively.
def palindrome(word):
  if len(word)==0:
    return "Nothing was entered. Please try again."
  elif len(word)==1:
    word="The given word/letter/phrase is a palindrome."
    return word
  elif len(word) == 2:
    if word[0]==word[1]:
      word="This is a palindrome."
      return word
    else:
      word="The given word/phrase is not a palindrome."
      return word
  elif word[0]==word[-1]:
    return palindrome(word[1:len(word)-1])
  else:
    return "The given word/phrase is not a palindrome."
print(palindrome(word))








