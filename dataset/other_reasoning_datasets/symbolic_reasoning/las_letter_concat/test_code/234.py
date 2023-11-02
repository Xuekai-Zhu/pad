def solution():
    s = "Manuel Aurelio India Rosalba"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())