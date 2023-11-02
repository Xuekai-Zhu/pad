def solution():
    s = "Alexa Pilar Rod Nicola"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())