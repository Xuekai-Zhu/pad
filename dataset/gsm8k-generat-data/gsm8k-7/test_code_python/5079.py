def solution():
    ticket_price = 10.0
    combo_price = 11.0
    candy_price = 2.5
    num_candies = 2

    # Calculate the total cost of the tickets
    total_tickets_cost = ticket_price * 2

    # Calculate the total cost of the combo meal
    total_combo_cost = combo_price

    # Calculate the total cost of the candy
    total_candy_cost = num_candies * candy_price

    # Calculate the total cost of the date
    total_cost = total_tickets_cost + total_combo_cost + total_candy_cost
    result = total_cost
    return result

print(solution())