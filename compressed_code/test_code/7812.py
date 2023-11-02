def solution():
    
    mars_other = 150
    mars_total = mars_other / 0.3
    moon_total = mars_total / 2
    moon_iron = moon_total * 0.5
    moon_carbon = moon_total * 0.2
    moon_other = moon_total * 0.3
    result = moon_total
    return result

print(solution())