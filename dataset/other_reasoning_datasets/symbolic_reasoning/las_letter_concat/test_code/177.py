def solution():
    s = "Donnie Alli Terry Krystal"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())