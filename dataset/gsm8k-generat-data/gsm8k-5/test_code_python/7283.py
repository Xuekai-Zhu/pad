def solution():
    # Calculate the number of rows needed for the bean seedlings
    bean_rows = 64 / 8

    # Calculate the number of rows needed for the pumpkin seeds
    pumpkin_rows = 84 / 7

    # Calculate the number of rows needed for the radishes
    radish_rows = 48 / 6

    # Calculate the total number of rows
    total_rows = bean_rows + pumpkin_rows + radish_rows

    # Calculate the number of plant beds needed
    plant_beds = total_rows / 2
    result = plant_beds
    return result

print(solution())