def solution():
    s = "Luisa Tatiana Drake Hillary"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())