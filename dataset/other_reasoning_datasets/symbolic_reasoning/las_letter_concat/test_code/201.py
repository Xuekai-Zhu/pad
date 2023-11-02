def solution():
    s = "Andrés Miles Ronaldo Melinda"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())