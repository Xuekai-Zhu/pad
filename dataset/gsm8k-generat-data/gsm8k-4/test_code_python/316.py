def solution():
    """The selling price of a bicycle that had sold for $220 last year was increased by 15%. What is the new price?"""
    # Define the original price of the bicycle and the percentage increase
    original_price = 220
    increase_percentage = 15

    # Calculate the amount of the increase
    increase_amount = original_price * (increase_percentage / 100)

    # Calculate the new price by adding the increase to the original price
    new_price = original_price + increase_amount

    # Return the result
    result = new_price
    return result

print(solution())