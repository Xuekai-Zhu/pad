def solution():
    s = "Rohan Antoinette Nikki Aida"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())