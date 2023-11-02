def solution():
    """Isabela bought twice as many cucumbers as pencils, with both costing $20 each. If she got a 20% discount on the pencils and bought 100 cucumbers, calculate the total amount she spent to buy the items."""

    # Total cost of pencils before discount
    pencil_cost_without_discount = 20 * x

    # Total cost of pencils after discount
    pencil_cost_with_discount = 0.8 * pencil_cost_without_discount

    # Total cost of cucumbers
    cucumber_cost = 20 * 2 * 100

    # Total amount spent by Isabela
    total_cost = pencil_cost_with_discount + cucumber_cost

    result = total_cost
    return result

print(solution())