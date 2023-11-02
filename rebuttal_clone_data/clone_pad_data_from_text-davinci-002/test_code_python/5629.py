def solution():
    vaccinated = 1/3
    recovered = 1/3
    both = 1/6
    
    immune = vaccinated + recovered + both
    result = immune
    
    return result

print(solution())