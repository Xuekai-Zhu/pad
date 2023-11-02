def solution():
    total_water = 1200
    first_neighborhood = 150
    second_neighborhood = first_neighborhood * 2
    third_neighborhood = second_neighborhood + 100

    # Calculate the total water used by the first three neighborhoods
    total_used = first_neighborhood + second_neighborhood + third_neighborhood

    # Calculate the water left for the fourth neighborhood
    water_left = total_water - total_used
    result = water_left
    return result

print(solution())