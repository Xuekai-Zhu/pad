def solution():
    s = "Maxwell Jose Beto Joe"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())