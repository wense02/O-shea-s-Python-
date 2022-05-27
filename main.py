# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

    # openfile = open("./story.txt","r")
def read_file_content(filename):
     #reading the files
    with open("./story.txt","r") as openfile:
         read_file = openfile.read()
    return read_file
          
         
def countwords():
    text = read_file_content("./story.txt")
    split_text = text.split()
    #print(split_text)
    count ={}
    for i in split_text:
        if i in count:
            count[i] +=1
        else:
            count[i] =1
    return count


print(countwords())