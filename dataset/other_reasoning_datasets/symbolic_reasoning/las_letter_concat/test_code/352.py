def solution():
    s = "Barbie Desiree Yaneth Dre"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())