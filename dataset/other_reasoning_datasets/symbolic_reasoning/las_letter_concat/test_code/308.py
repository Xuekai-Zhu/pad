def solution():
    s = "Jodi Judi Nia Raj"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())