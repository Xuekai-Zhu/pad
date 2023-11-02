def solution():
    """Isabela bought twice as many cucumbers as pencils, with both costing $20 each. If she got a 20% discount on the pencils and bought 100 cucumbers, calculate the total amount she spent to buy the items."""
    # Define the cost of each item
    ITEM_COST = 20

    # Define the number of cucumbers purchased
    cucumber_count = 100

    # Calculate the number of pencils purchased
    pencil_count = cucumber_count / 2

    # Calculate the cost of the pencils before the discount
    pencil_cost_before_discount = pencil_count * ITEM_COST

    # Calculate the discount on the pencils
    pencil_discount = 0.2 * pencil_cost_before_discount

    # Calculate the cost of the pencils after the discount
    pencil_cost_after_discount = pencil_cost_before_discount - pencil_discount

    # Calculate the total cost of the items
    total_cost = (cucumber_count * ITEM_COST) + pencil_cost_after_discount

    # Display the total cost
    result = total_cost
    return result

print(solution())