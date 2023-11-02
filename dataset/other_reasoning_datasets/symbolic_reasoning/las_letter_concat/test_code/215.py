def solution():
    s = "Ramona Lucy Gail Octavio"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())