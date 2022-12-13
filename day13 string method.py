a="!!Sid!!!!  !!!! Asta!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Sid","Naruto"))
print(a.split(" "))
blogheading="welcome to my world"
print(blogheading.capitalize())#capital first letter of 1st word
str1="welcome to console!!!"
str2="welcometoconsole"
str3="welcome to \nconsole!!!"
str4="  "
str5="Welcome To Console!!!"
print(str1.center(50))
print(len(str1.center(50)))
print(a.count("!"))
print(str1.endswith("!"))#check if str end with that char
print(str1.endswith("to",4,10))#str strating from 4 to 10 ends with "to"so true
print(blogheading.find("to"))#find 1st occurance of str, returns -1 if str not found
print(blogheading.index("my"))#find index
print(str2.isalnum())#alphanumeric
print(str2.isalpha())#only aphabets
print(str2.islower())#checks if str is lower
print(str3.isprintable())#checks if str is printable, \n is not printable so returned false
print(str4.isspace())#checks if only white spaces is present
print(str5.istitle())#checks if every word starts with capital
print(str1.swapcase())#swap the case(upper/lower)
print(str1.title())#makes every 1st letter of str capital