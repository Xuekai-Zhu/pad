def solution():
    s = "Memo Joey Phil Samuel"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())