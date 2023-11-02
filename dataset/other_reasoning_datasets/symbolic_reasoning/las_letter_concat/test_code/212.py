def solution():
    s = "Lesley Luna Nadia Adriana"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())