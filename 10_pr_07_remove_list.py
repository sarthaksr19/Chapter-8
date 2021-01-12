def remove_and_strip(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()


l1 = "    Sarthak is a good boy       "
n = remove_and_strip(l1,"Sarthak")
print(n)