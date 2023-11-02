def solution():
    s = "Donovan Lonnie Jairo Mariah"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())