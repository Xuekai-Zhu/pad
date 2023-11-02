def solution():
    ticket_cost = 300
    hotel_cost = ticket_cost / 2
    starting_money = 760

    # Calculate the total amount spent on the trip
    total_spent = ticket_cost + hotel_cost

    # Calculate how much money Maria has left
    remaining_money = starting_money - total_spent
    result = remaining_money
    return result

print(solution())