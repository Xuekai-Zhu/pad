def solution():
    s = "Yasmin Yesenia Carmela Susie"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())