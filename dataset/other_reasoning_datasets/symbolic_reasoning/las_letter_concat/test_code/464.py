def solution():
    s = "Jeremiah Kelley Josue Veronica"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())