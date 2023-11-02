def solution():
    s = "Jeannie Kenneth Porfirio Ezequiel"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())