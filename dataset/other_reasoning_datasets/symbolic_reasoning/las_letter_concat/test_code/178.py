def solution():
    s = "Carlos Jackie Callie Caitlin"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())