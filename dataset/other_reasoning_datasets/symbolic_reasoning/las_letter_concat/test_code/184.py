def solution():
    s = "Jose Luis Kiara Arun Josefina"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())