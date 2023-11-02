def solution():
    s = "Janette Stacey Ronny Kim"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())