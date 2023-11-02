def solution():
    s = "Margaret Rosi Willy Charlene"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())