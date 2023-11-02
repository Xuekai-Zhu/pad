def solution():
    s = "Rocio Sandy Anahi Latasha"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())