def solution():
    s = "Sandeep Graciela Jai Xiomara"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())