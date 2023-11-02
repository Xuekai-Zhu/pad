def solution():
    # Calculate the total number of blossoms in Mario's garden
    first_plant = 2  # first hibiscus plant has 2 flowers
    second_plant = 2 * first_plant  # second plant has twice as many flowers as the first
    third_plant = 4 * second_plant  # third plant has four times as many flowers as the second
    total_blossoms = first_plant + second_plant + third_plant
    result = total_blossoms
    return result

print(solution())