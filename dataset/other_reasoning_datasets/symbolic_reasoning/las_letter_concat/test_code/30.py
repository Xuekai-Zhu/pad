def solution():
    s = "Mauricio Lee Madi Lizzie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())