def solution():
    s = "Guillermina Evelin Dominique Johnny"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())