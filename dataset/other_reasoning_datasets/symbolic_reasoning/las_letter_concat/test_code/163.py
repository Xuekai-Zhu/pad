def solution():
    s = "Connie Elena Tami Stuart"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())