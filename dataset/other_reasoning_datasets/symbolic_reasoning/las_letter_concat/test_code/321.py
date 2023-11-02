def solution():
    s = "Hazel Gabrielle Tre Dalton"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())