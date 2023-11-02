def solution():
    s = "Wilmer Valerie Melissa Eloisa"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())