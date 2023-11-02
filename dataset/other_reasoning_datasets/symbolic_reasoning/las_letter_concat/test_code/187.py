def solution():
    s = "Bret Lois Ismael Mirna"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())