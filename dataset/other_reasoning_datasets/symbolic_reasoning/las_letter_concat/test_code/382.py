def solution():
    s = "Yazmin Lea Rodrigo Sammy"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())