def solution():
    s = "Cinthia Lloyd Jacqueline Jc"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())