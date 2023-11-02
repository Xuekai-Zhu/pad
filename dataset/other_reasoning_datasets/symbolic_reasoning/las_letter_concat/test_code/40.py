def solution():
    s = "Skylar Chrissy Misty Kike"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())