def solution():
    s = "Micaela Kevin Diamond Ty"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())