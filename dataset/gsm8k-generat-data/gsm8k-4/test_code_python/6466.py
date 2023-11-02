def solution():
    """It’s spring! The gardener at Parc Municipal orders flowers. He takes 250 tulips, 375 carnations and 320 roses. Each flower is sold for 2€. Calculate the total expenses."""
    # Define the number of tulips, carnations, and roses
    num_tulips = 250
    num_carnations = 375
    num_roses = 320

    # Calculate the total number of flowers
    total_flowers = num_tulips + num_carnations + num_roses

    # Calculate the total expenses of the flowers
    total_expenses = total_flowers * 2

    # Return the result
    result = total_expenses
    return result

print(solution())