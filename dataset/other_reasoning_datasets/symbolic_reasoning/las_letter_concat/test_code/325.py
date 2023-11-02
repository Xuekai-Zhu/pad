def solution():
    s = "Sonya Eddy Carol Yung"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())