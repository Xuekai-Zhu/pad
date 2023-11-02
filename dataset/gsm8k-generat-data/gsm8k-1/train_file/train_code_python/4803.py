def solution():
    """Isabela bought twice as many cucumbers as pencils, with both costing $20 each. If she got a 20% discount on the pencils and bought 100 cucumbers, calculate the total amount she spent to buy the items."""
    total_items = 100 + 100/2
    cucumber_cost = 20
    pencil_cost = 20 * 0.8 #20% discount
    total_cost = (cucumber_cost * 100) + (pencil_cost * 100/2)
    result = total_cost
    return result

print(solution())