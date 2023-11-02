def solution():
    s = "Evelyn Mason Shelby Aldo"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())