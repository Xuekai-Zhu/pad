def solution():
    number_of_tickets = 4  # Daria wants to buy tickets for herself and three friends
    ticket_cost = 90  # One ticket costs $90
    current_money = 189  # Daria currently has $189

    # Calculate the total cost of the tickets
    total_cost = number_of_tickets * ticket_cost

    # Calculate how much more money Daria needs to earn
    remaining_money = total_cost - current_money
    result = remaining_money
    return result

print(solution())