def solution():
    s = "Edwin Lovely Curt Damon"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())