def solution():
    s = "Albert Felicia Margo Patty"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())