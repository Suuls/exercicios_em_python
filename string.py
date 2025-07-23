## A partir da string “!! ! a;b;c;d;e;f;gh!#########” gere o resultado
## ['a', 'b', 'c', 'd', 'e', 'f', 'g']

string = "!! ! a;b;c;d;e;f;gh!#########"
print(string)
print(string.strip(" !#h").split(";"))
