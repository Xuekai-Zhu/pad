def solution():
    s = "Maritza Nana Loretta Eric"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())