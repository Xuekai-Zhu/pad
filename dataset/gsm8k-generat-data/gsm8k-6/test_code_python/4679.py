def solution():
    # Calculate the number of baby sea turtles that got swept to the sea
    swept_to_sea = 42 / 3  

    # Calculate the number of baby sea turtles remaining on the sand
    remaining_on_sand = 42 - swept_to_sea
    result = remaining_on_sand
    return result

print(solution())