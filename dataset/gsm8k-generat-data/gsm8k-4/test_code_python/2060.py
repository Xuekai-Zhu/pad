def solution():
    """Daisy’s milk cow provides 16 cups of milk per day.  75% of the milk is consumed by Daisy’s kids.  Daisy uses 50% of the remaining milk to cook with.  How much milk is left over?"""
    # Define the total amount of milk provided by the cow each day
    total_milk = 16

    # Calculate the amount of milk consumed by Daisy's kids
    kids_milk = total_milk * 0.75

    # Calculate the amount of milk left after the kids have their share
    remaining_milk = total_milk - kids_milk

    # Calculate the amount of milk used for cooking
    cooking_milk = remaining_milk * 0.5

    # Calculate the amount of milk left over
    leftover_milk = remaining_milk - cooking_milk

    result = leftover_milk
    return result

print(solution())