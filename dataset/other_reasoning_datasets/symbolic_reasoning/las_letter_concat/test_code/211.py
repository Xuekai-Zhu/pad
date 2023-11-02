def solution():
    s = "Ubaldo Katrina Francis Lynn"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())