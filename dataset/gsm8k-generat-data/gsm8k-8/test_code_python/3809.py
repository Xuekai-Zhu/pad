def solution():
    # Define the number of T-shirts and sweaters Norma left in the washer
    t_shirts = 9
    sweaters = 2 * t_shirts

    # Define the number of T-shirts and sweaters Norma found when she returned
    t_shirts_found = 3 * sweaters
    sweaters_found = 3 * t_shirts

    # Calculate the total number of items
    total_items = t_shirts + sweaters

    # Calculate the total number of items Norma should have found
    total_items_found = t_shirts_found + sweaters_found

    # Calculate how many items are missing
    missing_items = total_items - total_items_found
    result = missing_items
    return result

print(solution())