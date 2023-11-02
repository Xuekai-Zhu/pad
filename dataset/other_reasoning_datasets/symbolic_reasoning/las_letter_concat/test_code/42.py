def solution():
    s = "Camilo Becky Eliza Rebecca"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())