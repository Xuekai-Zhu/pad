def solution():
    """Last week, a farmer shipped 10 boxes of pomelos which had 240 pomelos in all. This week, the farmer shipped 20 boxes. How many dozens of pomelos did the farmer ship in all?"""
    # Define the number of pomelos in each box
    POMELO_PER_BOX = 24

    # Calculate the total number of pomelos shipped in both weeks
    total_pomelos = 10 * POMELO_PER_BOX + 20 * POMELO_PER_BOX

    # Calculate the total number of dozens of pomelos shipped
    total_dozens = total_pomelos / 12

    # Display the total number of dozens of pomelos shipped
    result = total_dozens
    return result

print(solution())