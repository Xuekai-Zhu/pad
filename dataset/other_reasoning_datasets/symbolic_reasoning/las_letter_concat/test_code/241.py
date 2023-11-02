def solution():
    s = "Allyson Mara Jo Toni"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())