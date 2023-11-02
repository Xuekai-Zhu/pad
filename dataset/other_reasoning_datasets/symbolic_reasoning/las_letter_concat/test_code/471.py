def solution():
    s = "Jazmine Carmen Kitty Nina"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())