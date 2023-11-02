def solution():
    s = "Angelica Tariq Ursula Nena"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())