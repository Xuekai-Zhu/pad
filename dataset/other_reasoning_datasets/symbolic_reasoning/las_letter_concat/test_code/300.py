def solution():
    s = "Miriam Brandy Bertha Renato"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())