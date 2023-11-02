def solution():
    s = "Colton Dexter Katy Brayden"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())