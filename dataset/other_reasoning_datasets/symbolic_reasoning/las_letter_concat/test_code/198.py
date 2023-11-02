def solution():
    s = "Marcy Gonzalez Alice Arlene"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())