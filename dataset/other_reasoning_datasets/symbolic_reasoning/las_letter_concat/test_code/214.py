def solution():
    s = "Gabby Reese Leah Celia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())