def solution():
    s = "Nicky Eden James Matt"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())