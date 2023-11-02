def solution():
    s = "Rosendo Shayla Erica Georgia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())