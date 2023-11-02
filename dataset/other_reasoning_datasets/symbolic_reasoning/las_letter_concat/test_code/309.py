def solution():
    s = "Irvin Brittney Vince Lucas"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())