def solution():
    s = "Theo Sheila Mariana Esmeralda"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())