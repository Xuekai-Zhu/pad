def solution():
    # Calculate the number of plant beds for each type of vegetable
    num_bean_beds = 64 // 8
    num_pumpkin_beds = 84 // 7
    num_radish_beds = 48 // 6

    # Calculate the total number of plant beds
    total_beds = num_bean_beds + num_pumpkin_beds + num_radish_beds
    result = total_beds
    return result

print(solution())