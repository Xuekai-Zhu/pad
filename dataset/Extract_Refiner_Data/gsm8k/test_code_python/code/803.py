def solution():
    
    # Define the number of glass chips needed for one bag of glass chips
    CHIPS_PER_BAG = 72

    # Define the number of bags of glass chips Milo has
    num_bags = 2

    # Calculate the total number of glass chips Milo has
    total_chips = num_bags * CHIPS_PER_BAG

    # Calculate the total square inches of the mosaic
    total_inches = total_chips * 12

    # Display the total square inches of the mosaic
    result = total_inches
    return result

print(solution())