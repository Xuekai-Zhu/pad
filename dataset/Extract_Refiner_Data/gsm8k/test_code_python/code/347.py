def solution():
    
    # Define the number of plant pots asked for for the daisies and roses
    daisies_pots = 30
    roses_pots = daisies_pots * 2

    # Calculate the total number of plant pots needed
    total_pots = daisies_pots + roses_pots

    # Calculate the number of plant pots left over
    left_over_pots = 100 - total_pots

    # Display the number of plant pots left over
    result = left_over_pots
    return result

print(solution())