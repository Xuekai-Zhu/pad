def solution():
    # Define the number of plates and meatballs per plate
    num_plates = 3
    meatballs_per_plate = 3

    # Calculate the total number of meatballs
    total_meatballs = num_plates * meatballs_per_plate

    # Calculate the number of meatballs eaten by each son
    meatballs_eaten_per_son = 2/3 * meatballs_per_plate

    # Calculate the total number of meatballs eaten by all three sons
    total_meatballs_eaten = 3 * meatballs_eaten_per_son

    # Calculate the number of meatballs left on the plates
    meatballs_left = total_meatballs - total_meatballs_eaten
    result = meatballs_left
    return result

print(solution())