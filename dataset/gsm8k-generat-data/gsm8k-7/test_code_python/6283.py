def solution():
    num_tickets = 2  # James and Susan
    ticket_price = 100
    dinner_price = 120
    tip_percent = 0.3  # 30% tip
    num_hours_limo = 6
    limo_price_per_hour = 80

    # Calculate the total cost of tickets
    total_ticket_cost = num_tickets * ticket_price

    # Calculate the total cost of dinner, including tip
    total_dinner_cost = dinner_price + (dinner_price * tip_percent)

    # Calculate the total cost of the limo rental
    total_limo_cost = num_hours_limo * limo_price_per_hour

    # Calculate the overall cost
    total_cost = total_ticket_cost + total_dinner_cost + total_limo_cost
    result = total_cost
    return result

print(solution())