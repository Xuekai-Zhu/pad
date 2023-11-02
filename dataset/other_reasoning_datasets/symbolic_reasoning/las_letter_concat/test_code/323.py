def solution():
    s = "Isaac Reyes Carly Tania"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())