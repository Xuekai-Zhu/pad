def solution():
    """We harvested 405 kg of apples. 90 kg were used to make fruit juice and 60 kg were given to a restaurant. The rest was sold in 5 kg bags and their sale brought in $408. What was the selling price of one bag of apples?"""
    # Calculate the total amount of apples that were not given away or used for juice
    remaining_apples = 405 - 90 - 60

    # Calculate the total number of 5 kg bags that can be made with the remaining apples
    num_bags = remaining_apples // 5

    # Calculate the price per bag of apples
    price_per_bag = 408 / num_bags

    # Display the selling price of one bag of apples
    result = price_per_bag
    return result

print(solution())