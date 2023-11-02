def solution():
    # Calculate the total expenses
    ticket_price = 7
    num_tickets = 3
    popcorn_price = 1.5 * 2
    milk_tea_price = 3 * 3
    total_expenses = (ticket_price * num_tickets) + popcorn_price + milk_tea_price

    # Calculate each person's contribution
    num_people = 3
    contribution = total_expenses / num_people
    result = contribution
    return result

print(solution())