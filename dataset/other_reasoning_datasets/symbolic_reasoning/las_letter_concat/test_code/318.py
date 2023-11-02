def solution():
    s = "Gabino Kayla Laurie Familia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())