def solution():
    """Daisy’s milk cow provides 16 cups of milk per day.  75% of the milk is consumed by Daisy’s kids.  Daisy uses 50% of the remaining milk to cook with.  How much milk is left over?"""
    # Define the amount of milk provided per day
    MILK_PER_DAY = 16

    # Calculate the amount of milk consumed by Daisy's kids
    kids_milk = MILK_PER_DAY * 0.75

    # Calculate the amount of milk remaining after the kids consume their share
    remaining_milk = MILK_PER_DAY - kids_milk

    # Calculate the amount of milk Daisy uses to cook with
    cooking_milk = remaining_milk * 0.5

    # Calculate the amount of milk left over
    left_over_milk = remaining_milk - cooking_milk

    # Display the amount of milk left over
    result = left_over_milk
    return result

print(solution())