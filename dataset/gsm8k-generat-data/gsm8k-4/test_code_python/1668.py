def solution():
    """Jim has a pail with rocks in it. The average weight of a rock is 1.5 pounds. A local rock collector agrees to pay him $4 for every pound of rocks. If he makes $60 off the sale, how many rocks were in the bucket?"""
    # Define the price per pound of rocks
    PRICE_PER_POUND = 4

    # Define the average weight of a rock
    ROCK_WEIGHT = 1.5

    # Define the total earnings from selling the rocks
    total_earnings = 60

    # Calculate the total weight of rocks
    total_weight = total_earnings / PRICE_PER_POUND

    # Calculate the number of rocks
    num_rocks = int(total_weight / ROCK_WEIGHT)

    # Return the result
    result = num_rocks
    return result

print(solution())