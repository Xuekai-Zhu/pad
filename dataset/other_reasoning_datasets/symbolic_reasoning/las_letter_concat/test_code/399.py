def solution():
    s = "Wesley Marcelo Rodolfo Erick"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())