# Question 1 : WAP to take input 2 strings and check if string 1 is a prefix, postfix, or nothing from string 2
string_1 = input("Enter string 1: ").strip()
string_2 = input("Enter string 2: ").strip()
print(string_2.find(string_1))
if string_2[string_2.find(string_1)] == string_2[len(string_2)- len(string_1)]:
    print(f"{string_1} is a postfix of {string_2}")
elif string_2[string_2.find(string_1)] == string_2[len(string_1)]:
    print(f"{string_2} is a prefix of {string_2}")
else: 
    print('Nothing')


# Question 2 : WAP to read a string and
# i ) Print frequency of all characters
# ii) Word of highest length
# iii) The string in Title Case
# iv) Read the full name and print only the first letters and the last name
def question_2():
    
    
    def i():
        string = list(input("Enter the string: "))
        output = {}
        for i in range(len(string)):
            try: 
                output[string[i]] = output[string[i]] + 1
            except KeyError:
                output[string[i]] = 1
        print(output)
        
        
    def ii():
        string = input("Enter the string: ").split(" ")
        longest_word = ""
        for i in range(len(string)):
            if len(string[i]) > len(longest_word):
                longest_word = string[i]
        print(longest_word)
        
        
    def iii():
        string = input("Enter the string: ").split(" ")
        for i in range(len(string)):
            if string[i].istitle():
                print(string[i])
                
    
    def iv():
        string = input("Enter the string: ").split(" ")
        for i in range(len(string)):
            if i != len(string) - 1 :
                print(string[i][0], end = " ")
            else:
                print(string[i])


# Question : Print all the indexes of occurences of a substring in a string
string = (input("Enter the string: "))
sub_string = input("Enter the substring: ")
x=string.split(sub_string)
y = 0
for i in range(1,len(x)):
    
    y = len(sub_string) + len(x[i-1])+y
    print(y)
