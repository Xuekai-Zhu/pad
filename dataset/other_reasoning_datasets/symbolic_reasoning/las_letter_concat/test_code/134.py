def solution():
    s = "Ericka Aly Darius Reed"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())