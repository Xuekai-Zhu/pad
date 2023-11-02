def solution():
    s = "Ruben Bernardo Ariel Shelley"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())