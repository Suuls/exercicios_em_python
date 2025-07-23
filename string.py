# A partir da string “!! ! a;b;c;d;e;f;gh!#########” gere o resultado ['a', 'b', 'c', 'd', 'e', 'f', 'g']

string = "!! ! a;b;c;d;e;f;gh!#########"
print(string)
print(string.strip(" !#h").split(";"))

#A partir da string “ring ring! - hello!“ gere o resultado:

string = "ring ring! - hello!"
print(string)
print(string.strip("ring ring!"))