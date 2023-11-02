def solution():
    meatballs_per_plate = 3  # There are 3 meatballs on each spaghetti plate
    sons = 3  # Theresa has 3 sons

    # Calculate the total number of meatballs eaten by Theresa's sons
    total_meatballs_eaten = sons * (2/3) * meatballs_per_plate

    # Calculate the total number of meatballs remaining on their plates
    total_meatballs_remaining = (sons * meatballs_per_plate) - total_meatballs_eaten
    result = total_meatballs_remaining
    return result

print(solution())