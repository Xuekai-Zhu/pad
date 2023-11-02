def solution():
    s = "Maureen Fabian Claudette Peyton"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())