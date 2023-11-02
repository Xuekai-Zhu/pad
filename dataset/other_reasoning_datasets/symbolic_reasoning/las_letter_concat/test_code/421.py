def solution():
    s = "Braulio Staci Jocelyn Brittany"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())