def solution():
    base_premium = 50
    accident_increase = 0.1
    ticket_increase = 5
    num_accidents = 1
    num_tickets = 3

    # Calculate the additional percentage increase due to accidents
    accident_percent_increase = accident_increase * num_accidents

    # Calculate the additional increase due to tickets
    ticket_increase_total = num_tickets * ticket_increase

    # Calculate the total percentage increase
    total_percent_increase = base_premium * accident_percent_increase

    # Calculate the new premium
    new_premium = base_premium + total_percent_increase + ticket_increase_total
    result = new_premium
    return result

print(solution())