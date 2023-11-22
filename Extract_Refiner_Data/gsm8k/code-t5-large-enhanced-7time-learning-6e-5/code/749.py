def solution():
    
    # Define the number of glasses and plates in a dozen
    GLASS_PER_DOZEN = 12
    PLATE_PER_DOZEN = 12

    # Define the number of glasses and plates sent
    glasses_sent = 8 * GLASS_PER_DOZEN
    plates_sent = 4 * PLATE_PER_DOZEN

    # Calculate the number of glasses and plates that were broken
    glasses_broken = 10
    plates_broken = 6

    # Calculate the new total number of glasses and plates
    new_total = glasses_sent - glasses_broken + plates_sent - plates_broken

    # Display the new total number of glasses and plates
    result = new_total
    return result

print(solution())