def solution():
    s = "Russ Berta Mandy Lydia"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())