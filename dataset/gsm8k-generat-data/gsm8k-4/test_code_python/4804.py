def solution():
    """Isabela bought twice as many cucumbers as pencils, with both costing $20 each. If she got a 20% discount on the pencils and bought 100 cucumbers, calculate the total amount she spent to buy the items."""
    # Define the price of pencils and cucumbers
    PENCIL_PRICE = 20
    CUCUMBER_PRICE = 20

    # Calculate the number of pencils bought
    pencils_bought = 100 / 2

    # Calculate the discounted price of pencils
    pencils_discounted = PENCIL_PRICE * 0.8

    # Calculate the total cost of pencils and cucumbers
    total_cost = (pencils_discounted * pencils_bought) + (CUCUMBER_PRICE * 100)

    # Return the result
    result = total_cost
    return result

print(solution())