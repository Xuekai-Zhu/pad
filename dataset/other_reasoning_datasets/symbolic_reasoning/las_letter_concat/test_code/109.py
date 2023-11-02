def solution():
    s = "Donny Lucero Christopher Gregory"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())