def solution():
    s = "Williams Reza Ashton Lillian"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())