def solution():
    s = "Chuy Shane Jaden Maynor"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())