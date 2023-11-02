def solution():
    s = "Loren Wes Dean Hayley"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())