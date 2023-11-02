def solution():
    s = "Johan Damien Serena Grace"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())