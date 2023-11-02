def solution():
    s = "Emma Maryann Olga Nataly"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())