def solution():
    s = "Martha Elijah Dominic Tonya"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())