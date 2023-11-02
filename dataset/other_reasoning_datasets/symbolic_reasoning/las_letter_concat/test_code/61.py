def solution():
    s = "Manish Lu Karl Don"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())