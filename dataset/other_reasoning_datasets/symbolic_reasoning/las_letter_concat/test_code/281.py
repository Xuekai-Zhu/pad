def solution():
    s = "Lora Alberto Cathy Kara"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())