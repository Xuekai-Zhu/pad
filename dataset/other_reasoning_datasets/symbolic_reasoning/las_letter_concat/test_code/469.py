def solution():
    s = "Nichole Heriberto Darian Peter"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())