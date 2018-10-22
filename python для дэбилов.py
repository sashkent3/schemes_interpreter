def hooks(s):
    counter = 0
    for sym in s:
        if sym == '(':
            counter += 1
        elif sym == ')':
            counter -= 1
        if counter < 0:
            return False
    if counter != 0:
        return False
    return True