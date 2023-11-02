def solution():
    """At a gym, the blue weights are 2 pounds each, and the green weights are 3 pounds each. Harry put 4 blue weights and 5 green weights onto a metal bar. The bar itself weighs 2 pounds. What is the total amount of weight, in pounds, of Harry's custom creation?"""
    # Define the weight of each type of weight
    BLUE_WEIGHT = 2
    GREEN_WEIGHT = 3

    # Define the number of each type of weight used
    blue_weights = 4
    green_weights = 5

    # Define the weight of the metal bar
    bar_weight = 2

    # Calculate the total weight of the custom creation
    total_weight = (blue_weights * BLUE_WEIGHT) + (green_weights * GREEN_WEIGHT) + bar_weight

    # Display the total weight
    result = total_weight
    return result

print(solution())