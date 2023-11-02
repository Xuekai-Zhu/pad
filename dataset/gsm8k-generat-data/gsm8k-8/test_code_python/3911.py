def solution():
    # Define the volume of each jug and the fill percentage
    jug_volume = 2 # gallons
    fill_percent = 0.7

    # Calculate the volume of sand in each jug
    sand_volume = jug_volume * fill_percent

    # Calculate the weight of the sand in each jug
    sand_weight = sand_volume * 5 # 5 pounds/gallon

    # Calculate the total weight of the improvised weights
    total_weight = sand_weight * 2 # two jugs

    result = total_weight
    return result

print(solution())