def solution():
    s = "Gabe Dora Aileen Modesto"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())