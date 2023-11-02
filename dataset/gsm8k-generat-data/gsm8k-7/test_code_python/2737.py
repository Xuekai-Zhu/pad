def solution():
    children_monday = 7
    adults_monday = 5
    children_tuesday = 4
    adults_tuesday = 2
    child_ticket_price = 3
    adult_ticket_price = 4

    # Calculate the total revenue from Monday
    revenue_monday = (children_monday * child_ticket_price) + (adults_monday * adult_ticket_price)

    # Calculate the total revenue from Tuesday
    revenue_tuesday = (children_tuesday * child_ticket_price) + (adults_tuesday * adult_ticket_price)

    # Calculate the total revenue for both days
    total_revenue = revenue_monday + revenue_tuesday
    result = total_revenue
    return result

print(solution())