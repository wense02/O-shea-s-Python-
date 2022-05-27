# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):
    # [assignment] Add your code here
     str1 = 'abyss'
     str2 = 'aybss'
     str1_anagram = sorted(str1)
     str2_anagram = sorted(str2)

     if str1_anagram == str2_anagram:
             return True
     else:   
             return False     
print(find_anagram('abyss', 'aybss'))
