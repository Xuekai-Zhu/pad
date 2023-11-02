def solution():
    s = "Quinton Sam Soledad Becca"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())