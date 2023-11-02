def solution():
    s = "Shannon Millie Rosemary Priyanka"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())