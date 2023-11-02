def solution():
    s = "Elva Kari Shirley Gilberto"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())