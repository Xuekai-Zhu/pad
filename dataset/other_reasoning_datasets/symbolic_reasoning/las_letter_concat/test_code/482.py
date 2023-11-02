def solution():
    s = "Marco Antonio Suzette Roland Isabel"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())