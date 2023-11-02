def solution():
    """Jimmy has a collection of 5 action figures. Each figure is worth $15, except for one which is worth $20. He decided to sell his collection. To do it fast he decided to sell each of them for $5 less than their value. How much will Jimmy earn if he sells all the figures?"""
    # Define the original value of each figure
    FIGURE_VALUE = 15

    # Define the value of the special figure
    SPECIAL_VALUE = 20

    # Define the discount for each figure
    DISCOUNT = 5

    # Calculate the total value of the collection
    total_value = (FIGURE_VALUE * 4) + SPECIAL_VALUE

    # Calculate the discounted value of each figure
    discounted_value = FIGURE_VALUE - DISCOUNT

    # Calculate the total earnings if Jimmy sells all the figures
    total_earnings = (discounted_value * 4) + (SPECIAL_VALUE - DISCOUNT)

    # Display Jimmy's earnings
    result = total_earnings
    return result

print(solution())