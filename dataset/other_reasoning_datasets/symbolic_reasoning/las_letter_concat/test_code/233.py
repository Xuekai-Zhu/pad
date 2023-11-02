def solution():
    s = "Rachel Alisa Fanny Jeffery"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())