def solution():
    """There are 3 meatballs on each spaghetti plate. If Theresa's 3 sons each eat two-thirds of the meatballs on their respective plates, how many meatballs are still left on their plates altogether?"""
    # Define the number of meatballs on each plate and the number of sons
    meatballs_per_plate = 3
    num_sons = 3

    # Calculate the total number of meatballs
    total_meatballs = meatballs_per_plate * num_sons

    # Calculate the number of meatballs each son ate
    num_meatballs_eaten = (2/3) * meatballs_per_plate

    # Calculate the total number of meatballs eaten
    total_meatballs_eaten = num_meatballs_eaten * num_sons

    # Calculate the number of meatballs still on the plates
    meatballs_left = total_meatballs - total_meatballs_eaten

    # Return the result
    result = meatballs_left
    return result

print(solution())