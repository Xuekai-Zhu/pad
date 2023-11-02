def solution():
    """Teddy is a pillow-maker. He uses 3 less than 5 pounds of fluffy foam material to make each pillow. If Teddy has three tons of fluffy foam material, how many pillows can he make?"""
    fluffy_foam_per_pillow = 5 - 3
    tons_of_fluffy_foam = 3
    pounds_of_fluffy_foam = tons_of_fluffy_foam * 2000
    pillows = pounds_of_fluffy_foam // fluffy_foam_per_pillow
    result = pillows
    return result

print(solution())