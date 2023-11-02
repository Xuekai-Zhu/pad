def solution():
    s = "Orlando Colby Julius Ofelia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())