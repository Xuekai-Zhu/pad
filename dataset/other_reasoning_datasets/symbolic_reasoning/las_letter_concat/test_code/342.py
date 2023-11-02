def solution():
    s = "Yessenia Geraldine Minerva Tanya"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())