def solution():
    s = "Yan Eunice Joseph Hugh"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())