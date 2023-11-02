def solution():
    s = "Beatrice Taylor Juan Carlos Kaitlin"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())