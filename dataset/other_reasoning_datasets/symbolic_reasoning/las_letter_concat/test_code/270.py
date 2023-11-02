def solution():
    s = "Kristine Van Marisol Preston"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())