def solution():
    """Nellie had 380 legos, but she lost 57 of them and gave her sister 24 legos. How many legos does she have now?"""
    # Define the initial number of legos
    initial_legos = 380

    # Define the number of legos lost and given away
    lost_legos = 57
    given_legos = 24

    # Calculate the total number of legos currently owned
    current_legos = initial_legos - lost_legos - given_legos

    # Display the current number of legos
    result = current_legos
    return result

print(solution())