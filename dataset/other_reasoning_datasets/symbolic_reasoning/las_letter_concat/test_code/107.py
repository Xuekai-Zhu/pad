def solution():
    s = "Dalila Emily Casey Clifford"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())