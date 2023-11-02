def solution():
    # Calculate the total number of ice cubes Dylan used
    total_ice_cubes = 8 + 2*8  # Dylan put two times as many ice cubes in the pitcher as the number in his glass
    trays_needed = total_ice_cubes/12  # calculate the number of trays needed to fill all the ice they have
    result = math.ceil(trays_needed)  # rounds up to the nearest whole number to get the number of trays needed
    return result

print(solution())