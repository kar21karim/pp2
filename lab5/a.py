import re

def match_ab(s):
    pattern = r'^ab*$'
    return bool(re.match(pattern, s))

print(match_ab('a'))     
print(match_ab('abbbbbbbbb'))  
print(match_ab('ac'))    
