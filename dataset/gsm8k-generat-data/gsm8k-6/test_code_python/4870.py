def solution():
    # Calculate the total revenue of the concert
    adult_tickets = 183
    child_tickets = 28
    adult_price = 26
    child_price = 0.5 * adult_price
    total_revenue = (adult_tickets * adult_price) + (child_tickets * child_price)
    result = total_revenue
    return result

print(solution())