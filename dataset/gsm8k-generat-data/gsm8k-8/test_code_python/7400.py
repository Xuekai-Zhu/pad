def solution():
    # Define the fraction of the collection sold and the amount earned
    fraction_sold = 4/7
    amount_earned = 28

    # Calculate the total value of the collection
    total_value = amount_earned / fraction_sold

    # Calculate the amount Hana would have earned from selling the entire collection
    amount_from_entire_collection = total_value * (1 - fraction_sold)

    result = amount_from_entire_collection
    return result

print(solution())