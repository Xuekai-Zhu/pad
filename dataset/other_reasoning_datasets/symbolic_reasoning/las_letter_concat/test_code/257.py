def solution():
    s = "Maricruz Alfredo Barry Deepak"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())