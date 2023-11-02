def solution():
    s = "Lino Mariel Aditya Elisabeth"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())