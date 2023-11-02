def solution():
    s = "Lionel Fiona Bobby Janeth"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())