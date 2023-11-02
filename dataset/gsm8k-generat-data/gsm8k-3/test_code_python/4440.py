def solution():
    """Sherry is making banana bread for a bake sale. She wants to make 99 loaves. Her recipe makes enough batter for 3 loaves. The recipe calls for 1 banana. How many bananas does Sherry need?"""
    # Define the number of loaves the recipe makes batter for and the number of bananas needed per batter
    LOAVES_PER_BATTER = 3
    BANANAS_PER_BATTER = 1

    # Define the number of loaves Sherry wants to make
    NUM_LOAVES = 99

    # Calculate the number of batches of batter needed
    num_batches = NUM_LOAVES // LOAVES_PER_BATTER
    if NUM_LOAVES % LOAVES_PER_BATTER != 0:
        num_batches += 1

    # Calculate the total number of bananas needed
    total_bananas = num_batches * BANANAS_PER_BATTER

    # Display the total number of bananas needed
    result = total_bananas
    return result

print(solution())