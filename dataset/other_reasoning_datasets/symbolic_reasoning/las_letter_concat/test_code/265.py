def solution():
    s = "Teri Lina Mery Melanie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())