def solution():
    s = "Kali Jeanette Tess Devin"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())