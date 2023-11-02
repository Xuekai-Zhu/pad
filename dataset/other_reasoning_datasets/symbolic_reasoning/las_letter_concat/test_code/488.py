def solution():
    s = "Leigh Mindy Rocky Lex"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())