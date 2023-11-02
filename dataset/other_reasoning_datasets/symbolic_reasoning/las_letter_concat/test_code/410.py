def solution():
    s = "Delia Kathleen Mateo Marvin"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())