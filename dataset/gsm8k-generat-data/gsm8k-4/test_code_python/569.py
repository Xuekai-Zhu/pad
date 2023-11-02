def solution():
    """At a gym, the blue weights are 2 pounds each, and the green weights are 3 pounds each. Harry put 4 blue weights and 5 green weights onto a metal bar. The bar itself weighs 2 pounds. What is the total amount of weight, in pounds, of Harry's custom creation?"""
    # Define the weight of the blue weights and the number of blue weights
    BLUE_WEIGHT = 2
    blue_count = 4

    # Define the weight of the green weights and the number of green weights
    GREEN_WEIGHT = 3
    green_count = 5

    # Define the weight of the metal bar
    BAR_WEIGHT = 2

    # Calculate the total weight
    total_weight = (BLUE_WEIGHT * blue_count) + (GREEN_WEIGHT * green_count) + BAR_WEIGHT

    # Return the result
    result = total_weight
    return result

print(solution())