def solution():
    s = "Nidia Rachelle Lauren Shelia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())