def solution():
    # Calculate the total number of meatballs eaten by Theresa's sons
    total_meatballs_eaten = (2/3) * 3 * 3  # each son eats two-thirds of the meatballs on their plate, and there are 3 plates
    # Calculate the total number of meatballs remaining on the plates
    total_meatballs_remaining = 3 * 3 - total_meatballs_eaten  # there are 3 meatballs on each plate, and the total eaten by the sons is subtracted
    result = total_meatballs_remaining
    return result

print(solution())