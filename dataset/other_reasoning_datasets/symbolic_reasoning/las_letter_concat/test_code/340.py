def solution():
    s = "Ulises Derek Adrianna Eugene"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())