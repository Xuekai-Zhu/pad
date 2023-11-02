def solution():
    s = "Glenda Beverly Agustin Igor"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())