def solution():
    """Teddy is a pillow-maker. He uses 3 less than 5 pounds of fluffy foam material to make each pillow. If Teddy has three tons of fluffy foam material, how many pillows can he make?"""
    pounds_per_pillow = 5 - 3
    tons_of_foam = 3
    total_pillows = (tons_of_foam * 2000) / pounds_per_pillow
    result = total_pillows
    return result

print(solution())