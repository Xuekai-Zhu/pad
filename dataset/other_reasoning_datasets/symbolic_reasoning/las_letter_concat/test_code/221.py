def solution():
    s = "Armando Astrid Anibal Dakota"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())