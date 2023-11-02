def solution():
    s = "Louise Mariano Laura Gerardo"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())