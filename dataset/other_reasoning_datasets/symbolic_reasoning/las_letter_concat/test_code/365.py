def solution():
    s = "Caroline Demetrius Fidel Solomon"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())