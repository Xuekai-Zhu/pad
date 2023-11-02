def solution():
    s = "Michel Roy Sergey Jessie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())