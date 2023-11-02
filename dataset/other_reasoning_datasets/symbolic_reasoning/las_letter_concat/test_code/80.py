def solution():
    s = "Faustino Lamar Fransisco Rina"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())