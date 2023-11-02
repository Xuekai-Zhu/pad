def solution():
    s = "Efren Rex Marilyn Emerson"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())