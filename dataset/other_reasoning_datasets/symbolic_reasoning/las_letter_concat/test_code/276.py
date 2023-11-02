def solution():
    s = "Marcia Belen Reyna Britney"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())