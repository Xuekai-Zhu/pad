def solution():
    s = "Cristobal Dania Li Anna"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())