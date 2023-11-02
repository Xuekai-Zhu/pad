def solution():
    s = "Bobbi Tamika Zac Lala"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())