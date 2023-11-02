def solution():
    """Hana sold 4/7 of her stamp collection for $28. How much would she have earned from selling the entire collection?"""
    # Define the fraction of the stamp collection that was sold
    fraction_sold = 4/7

    # Define the amount earned from selling the fraction of the collection
    amount_sold = 28

    # Calculate the value of the entire collection by multiplying the amount earned by the reciprocal of the fraction sold
    value_collection = amount_sold / fraction_sold

    # return the result
    result = value_collection
    return result

print(solution())