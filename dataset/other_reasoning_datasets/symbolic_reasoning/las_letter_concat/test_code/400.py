def solution():
    s = "Sean Rebeca Marco Sami"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())