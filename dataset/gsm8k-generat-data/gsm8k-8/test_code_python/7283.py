def solution():
    # Calculate the number of bean rows
    num_bean_rows = 64/8

    # Calculate the number of pumpkin rows
    num_pumpkin_rows = 84/7

    # Calculate the number of radish rows
    num_radish_rows = 48/6

    # Calculate the total number of rows
    total_rows = num_bean_rows + num_pumpkin_rows + num_radish_rows

    # Calculate the number of plant beds
    num_plant_beds = total_rows / 2
    result = num_plant_beds
    return result

print(solution())