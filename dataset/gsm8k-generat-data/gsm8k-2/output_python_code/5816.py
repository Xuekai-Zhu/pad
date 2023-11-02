def solution():
    """Jenny wants to sell some girl scout cookies and has the choice of two neighborhoods to visit. Neighborhood A has 10 homes which each will buy 2 boxes of cookies. Neighborhood B has 5 homes, each of which will buy 5 boxes of cookies. Assuming each box of cookies costs $2, how much will Jenny make at the better choice of the two neighborhoods?"""
    neighborhoodA = 10 * 2 * 2
    neighborhoodB = 5 * 5 * 2
    if neighborhoodA > neighborhoodB:
        result = neighborhoodA
    else:
        result = neighborhoodB

    return result

print(solution())