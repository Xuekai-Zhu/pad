def solution():
    
    fluffy_foam_per_pillow = 5 - 3
    tons_of_fluffy_foam = 3
    pounds_of_fluffy_foam = tons_of_fluffy_foam * 2000
    pillows = pounds_of_fluffy_foam // fluffy_foam_per_pillow
    result = pillows
    return result

print(solution())