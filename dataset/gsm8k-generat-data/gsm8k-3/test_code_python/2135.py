def solution():
    """Janele wants to figure out the average weight of her cats. She has 4 of them. The first two weigh 12 pounds each. The third weighs 14.7 pounds and the fourth weighs 9.3 pounds. What is their average weight?"""
    # Define the weights of the four cats
    cat1_weight = 12
    cat2_weight = 12
    cat3_weight = 14.7
    cat4_weight = 9.3

    # Calculate the total weight of the cats
    total_weight = cat1_weight + cat2_weight + cat3_weight + cat4_weight

    # Calculate the average weight of the cats
    average_weight = total_weight / 4

    # Display the average weight
    result = average_weight
    return result

print(solution())