def solution():
    s = "Brooklyn Dawn Tay Gene"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())