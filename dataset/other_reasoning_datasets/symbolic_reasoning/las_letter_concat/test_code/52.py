def solution():
    s = "Imelda Andi Mack Rigoberto"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())