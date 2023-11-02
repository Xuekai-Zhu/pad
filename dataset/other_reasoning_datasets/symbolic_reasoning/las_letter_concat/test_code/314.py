def solution():
    s = "Daryl Owen Myra Aaron"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())