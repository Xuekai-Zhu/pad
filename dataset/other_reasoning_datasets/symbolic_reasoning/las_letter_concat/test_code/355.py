def solution():
    s = "Corey Elvin Tino Melvin"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())