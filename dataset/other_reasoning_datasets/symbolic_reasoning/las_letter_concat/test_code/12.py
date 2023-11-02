def solution():
    s = "Hank Janine Frankie Isa"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())