def solution():
    s = "Guadalupe Ebony Wil Luke"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())