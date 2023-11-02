def solution():
    s = "Bailey Lourdes Brianna Martín"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())