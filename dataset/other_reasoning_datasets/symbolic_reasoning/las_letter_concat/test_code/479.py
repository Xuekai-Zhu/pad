def solution():
    s = "Charmaine Vic Homero Jeanine"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())