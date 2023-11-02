def solution():
    iron = 50
    carbon = 20
    mars_weight = 150
    moon_weight = (mars_weight / 2) - (mars_weight * ((iron + carbon) / 100))
    result = moon_weight
    
    return result

print(solution())