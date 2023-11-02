def solution():
    s = "Fred Nolan Johnathan Carson"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())