def solution():
    # Define ticket prices and discount
    child_ticket_price = 4.25
    adult_ticket_price = child_ticket_price + 3.25
    discount = 2

    # Calculate total cost without discount
    total_cost = 2 * adult_ticket_price + 4 * child_ticket_price

    # Apply discount if applicable
    if total_cost >= 3 * child_ticket_price:
        total_cost -= discount

    result = total_cost
    return result

print(solution())