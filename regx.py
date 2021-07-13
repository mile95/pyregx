def matchOne(pattern: str, text: str) -> bool:
    if not text: return True
    if not pattern: return False
    if pattern == ".": return True
    return pattern == text

def match(pattern: str, text: str) -> bool:
    if pattern  == "": return True
    return matchOne(pattern[0], text[0]) and match(pattern[1:], text[1:])

print(matchOne('a', 'a'))
print(matchOne('.', 'z'))
print(matchOne('', 'h'))
print(matchOne('a', 'b'))
print(matchOne('p', ''))

print(match('a.c', 'abc'))