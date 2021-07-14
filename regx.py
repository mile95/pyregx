def matchOne(pattern: str, text: str) -> bool:
    if not text: return True
    if not pattern: return False
    if pattern == '.': return True
    return pattern == text

def match(pattern: str, text: str) -> bool:
    if pattern  == "": return True
    if pattern == '$' and text == "": return True
    return matchOne(pattern[0], text[0]) and match(pattern[1:], text[1:])

def search(pattern: str, text: str) -> bool:
    if pattern[0] == '^':
        return match(pattern[1:], text)
    return True in [match(pattern, text[x:]) for x in range(len(text)) ]

print(search("bc", "abcd"))

print(matchOne('a', 'a'))
print(matchOne('.', 'z'))
print(matchOne('', 'h'))
print(matchOne('a', 'b'))
print(matchOne('p', ''))

print(match('a.c', 'abc'))
