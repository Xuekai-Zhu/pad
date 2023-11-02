def solution():
    s = "Vicki Dwight Johnson Alexandra"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())