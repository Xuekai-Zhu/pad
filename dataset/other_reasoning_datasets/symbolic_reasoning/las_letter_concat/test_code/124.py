def solution():
    s = "Altagracia Howard Patti Douglas"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())