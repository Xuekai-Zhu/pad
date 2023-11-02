def solution():
    num_plates = 3
    num_meatballs_per_plate = 3
    fraction_eaten = 2/3

    # Calculate the total number of meatballs eaten
    total_meatballs_eaten = num_plates * num_meatballs_per_plate * fraction_eaten

    # Calculate the total number of meatballs still on the plates
    total_meatballs_left = (num_plates * num_meatballs_per_plate) - total_meatballs_eaten
    result = total_meatballs_left
    return result

print(solution())