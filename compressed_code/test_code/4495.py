def solution():
    
    neighborhoodA = 10 * 2 * 2
    neighborhoodB = 5 * 5 * 2
    if neighborhoodA > neighborhoodB:
        result = neighborhoodA
    else:
        result = neighborhoodB

    return result

print(solution())