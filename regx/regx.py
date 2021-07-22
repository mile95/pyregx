def matchOne(pattern: str, text: str) -> bool:
    if not pattern:
        return True
    if not text:
        return False
    if pattern == ".":
        return True
    return pattern == text


def matchQuestion(pattern: str, text: str) -> bool:
    # If the char before ? is matched
    if len(text) > 0 and matchOne(pattern[0], text[0]) and match(pattern[2:], text[1:]):
        return True
    # If the char before ? is not matched
    return match(pattern[2:], text)


def match(pattern: str, text: str) -> bool:
    if pattern == "":
        return True
    if pattern == "$" and text == "":
        return True
    if len(pattern) > 1 and pattern[1] == "?":
        return matchQuestion(pattern, text)
    return matchOne(pattern[0], text[0]) and match(pattern[1:], text[1:])


def search(pattern: str, text: str) -> bool:
    if pattern[0] == "^":
        return match(pattern[1:], text)
    if len(text) == 0:
        return match(pattern, text)
    return True in [match(pattern, text[x:]) for x in range(len(text))]
