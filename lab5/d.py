import re

def uppercase(s):
    pattern = r'^[A-Z][a-z]+$'
    return bool(re.match(pattern, s))

print(uppercase('Python'))  
print(uppercase('python'))  
