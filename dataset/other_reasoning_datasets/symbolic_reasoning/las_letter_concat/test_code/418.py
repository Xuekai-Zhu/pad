def solution():
    s = "Earl Rudy Harrison Nadine"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())