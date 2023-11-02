def solution():
    """There are 3 meatballs on each spaghetti plate.  If Theresa's 3 sons each eat two-thirds of the meatballs on their respective plates, how many meatballs are still left on their plates altogether?"""
    # Define the number of meatballs on each plate
    MEATBALLS_PER_PLATE = 3

    # Define the fraction of meatballs each son eats
    FRACTION_EATEN = 2/3

    # Calculate the total number of meatballs eaten by all 3 sons
    total_eaten = 3 * FRACTION_EATEN * MEATBALLS_PER_PLATE

    # Calculate the number of meatballs remaining on all 3 plates
    remaining = 3 * MEATBALLS_PER_PLATE - total_eaten

    # Display the number of meatballs remaining
    result = remaining
    return result

print(solution())