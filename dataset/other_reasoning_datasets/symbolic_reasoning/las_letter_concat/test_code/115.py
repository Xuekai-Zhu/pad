def solution():
    s = "Sid Isabelle Jackson Heidy"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())