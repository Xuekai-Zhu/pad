def solution():
    s = "Carissa Paige Consuelo Izzy"
    words = s.split()
    result = ''.join(word[-1] for word in words)
    return result

print(solution())