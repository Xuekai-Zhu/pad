def solution():
    
    # Define the number of packs and pieces of sweets per pack
    PACKS = 15
    SWEETS_PER_PACK = 60

    # Calculate the total number of sweets
    total_sweets = PACKS * SWEETS_PER_PACK

    # Calculate the number of sweets kept
    sweets_kept = 2 * SWEETS_PER_PACK

    # Calculate the number of sweets given to her friends
    sweets_given = total_sweets - sweets_kept

    # Calculate the number of sweets each friend received
    sweets_per_friend = sweets_given // 10

    # Display the number of sweets each friend received
    result = sweets_per_friend
    return result

print(solution())