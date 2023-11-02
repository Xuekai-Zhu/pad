def solution():
    s = "Gus Brock Ava Jenna"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())