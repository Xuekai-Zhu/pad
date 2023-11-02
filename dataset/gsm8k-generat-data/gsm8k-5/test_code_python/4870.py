def solution():
    ticket_price_adult = 26  # The ticket price for adults is $26
    ticket_price_child = ticket_price_adult / 2  # The ticket price for children is half of that for adults
    total_adults = 183  # 183 adults attended the concert
    total_children = 28  # 28 children attended the concert

    # Calculate the revenue from adult tickets
    revenue_adult = ticket_price_adult * total_adults

    # Calculate the revenue from child tickets
    revenue_child = ticket_price_child * total_children

    # Calculate the total revenue from ticket sales
    total_revenue = revenue_adult + revenue_child
    result = total_revenue
    return result

print(solution())