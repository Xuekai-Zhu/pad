def solution():
    s = "Conor Randall Oleg Stephanie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())