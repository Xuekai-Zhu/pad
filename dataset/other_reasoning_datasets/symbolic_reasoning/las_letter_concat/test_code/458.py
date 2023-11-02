def solution():
    s = "Sunny Trisha Paul Guy"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())