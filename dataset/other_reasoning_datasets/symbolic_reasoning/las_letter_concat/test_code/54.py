def solution():
    s = "Marian Joanne Darrin Rohit"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())