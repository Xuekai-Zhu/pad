def solution():
    s = "Alain Jerome Kristina Ida"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())