def solution():
    s = "Roberta Mauro Clint Marcela"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())