def solution():
    s = "Gabi Dante Rafa Tricia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())