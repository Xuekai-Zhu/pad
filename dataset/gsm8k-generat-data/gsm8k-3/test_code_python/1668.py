def solution():
    """Jim has a pail with rocks in it. The average weight of a rock is 1.5 pounds. A local rock collector agrees to pay him $4 for every pound of rocks. If he makes $60 off the sale, how many rocks were in the bucket?"""
    # Define the average weight of a rock and price per pound
    WEIGHT_PER_ROCK = 1.5
    PRICE_PER_POUND = 4

    # Define the total earnings from selling the rocks
    total_earnings = 60

    # Calculate the total weight of the rocks
    total_weight = total_earnings / PRICE_PER_POUND

    # Calculate the total number of rocks
    total_rocks = total_weight / WEIGHT_PER_ROCK

    # Display the total number of rocks
    result = total_rocks
    return result

print(solution())