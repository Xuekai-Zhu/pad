def solution():
    s = "Fausto Tito Jade Terrance"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())