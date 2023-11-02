def solution():
    s = "Clarissa Shauna Alexis Branden"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())