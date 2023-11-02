def solution():
    s = "Janice Shelly Arnulfo Nestor"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())