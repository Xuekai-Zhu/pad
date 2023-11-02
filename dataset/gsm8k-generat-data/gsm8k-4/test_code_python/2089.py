def solution():
    """Sophia ate 1/6 of her pie and she put the rest on the fridge. If the pie left in the fridge weighs 1200 grams, how many grams did Sophia eat?"""
    # Define the fraction of the pie that Sophia ate
    fraction_eaten = 1 / 6

    # Calculate the total weight of the pie before Sophia ate it
    total_weight = 1200 / fraction_eaten

    # Calculate the weight of the portion of the pie that Sophia ate
    eaten_weight = total_weight - 1200

    # return the result
    result = eaten_weight
    return result

print(solution())