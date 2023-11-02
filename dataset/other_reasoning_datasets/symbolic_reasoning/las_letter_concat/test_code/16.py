def solution():
    s = "Jessy Libby Danielle Red"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())