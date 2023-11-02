def solution():
    monday_price = 5  # Monday movie ticket price is $5
    wednesday_price = 2 * monday_price  # Wednesday movie ticket price is twice as much as Monday
    saturday_price = 5 * monday_price  # Saturday movie ticket price is five times as much as Monday
    glenn_tickets = [(wednesday_price, 1), (saturday_price, 1)]  # Glenn attends the movies on Wednesday and Saturday

    # Calculate the total cost of movie tickets for Glenn
    total_cost = sum([price * quantity for price, quantity in glenn_tickets])
    result = total_cost
    return result

print(solution())