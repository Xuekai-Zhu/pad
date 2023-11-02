def solution():
    s = "Gisela Gerald Mackenzie Ashley"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())