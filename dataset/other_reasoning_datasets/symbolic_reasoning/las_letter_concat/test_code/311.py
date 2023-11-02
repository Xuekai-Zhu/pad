def solution():
    s = "Renata Mariela Mona Kristin"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())