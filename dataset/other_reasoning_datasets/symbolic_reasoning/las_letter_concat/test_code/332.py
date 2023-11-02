def solution():
    s = "Flora Warren Gwendolyn Alissa"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())