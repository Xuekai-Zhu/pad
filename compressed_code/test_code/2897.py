def solution():
    
    total_acres = 60
    good_soil_acres = total_acres * (2/3)
    clay_soil_acres = total_acres * (1/3)
    good_soil_yield = 400
    clay_soil_yield = good_soil_yield / 2
    total_yield = (good_soil_acres * good_soil_yield) + (clay_soil_acres * clay_soil_yield)
    result = total_yield
    return result

print(solution())