def solution():
    """Janele wants to figure out the average weight of her cats. She has 4 of them. The first two weigh 12 pounds each. The third weighs 14.7 pounds and the fourth weighs 9.3 pounds. What is their average weight?"""
    # Define the weights of the cats
    weights = [12, 12, 14.7, 9.3]

    # Calculate the total weight
    total_weight = sum(weights)

    # Calculate the average weight
    average_weight = total_weight / len(weights)

    # return the result
    result = average_weight
    return result

print(solution())