def solution():
    s = "Dorian Mayra Freddie Magaly"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())