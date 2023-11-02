def solution():
    s = "Steph Pablo Ceci Francine"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())