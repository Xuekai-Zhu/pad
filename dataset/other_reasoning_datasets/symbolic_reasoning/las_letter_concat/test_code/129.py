def solution():
    s = "Raymundo Jonathon Lexi Rony"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())