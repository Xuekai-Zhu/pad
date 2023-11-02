def solution():
    s = "Bill Santos Roxy Randi"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())