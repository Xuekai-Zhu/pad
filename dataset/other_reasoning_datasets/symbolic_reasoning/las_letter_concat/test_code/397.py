def solution():
    s = "Bernie Melina Kelsey Rusty"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())