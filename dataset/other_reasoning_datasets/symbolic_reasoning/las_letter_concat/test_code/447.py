def solution():
    s = "Debby Geoffrey Alana Silvestre"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())