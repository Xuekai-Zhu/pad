def solution():
    """Six Grade 4 sections launched a recycling drive where they collect old newspapers to recycle. Each section collected 280 kilos in two weeks. After the third week, they found that they need 320 kilos more to reach their target. How many kilos of the newspaper is their target?"""
    # Define the number of sections and the amount collected per section
    NUM_SECTIONS = 6
    COLLECTION_PER_SECTION = 280

    # Calculate the total amount collected in the first two weeks
    total_collected = NUM_SECTIONS * COLLECTION_PER_SECTION * 2

    # Calculate the target amount
    target_amount = total_collected + 320

    # Display the target amount
    result = target_amount
    return result

print(solution())