def solution():
    s = "Cat Alisha Ramon Norberto"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())