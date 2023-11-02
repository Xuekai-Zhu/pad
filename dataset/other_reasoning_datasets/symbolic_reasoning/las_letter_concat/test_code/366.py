def solution():
    s = "Julio Sidney Aiden Shay"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())