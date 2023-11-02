def solution():
    s = "Juan Jose Dalia Destiny Amelia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())