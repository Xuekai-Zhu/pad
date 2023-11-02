def solution():
    s = "Alexandria Meghan Autumn Robert"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())