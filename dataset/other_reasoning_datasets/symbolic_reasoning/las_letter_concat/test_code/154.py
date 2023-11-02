def solution():
    s = "Myriam José Cecy Faisal"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())