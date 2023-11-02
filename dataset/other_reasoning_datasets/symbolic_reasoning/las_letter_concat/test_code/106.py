def solution():
    s = "Charity Svetlana Jamie Jose A"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())