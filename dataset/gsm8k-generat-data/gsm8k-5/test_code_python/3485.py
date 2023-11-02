def solution():
    ticket_cost = 300  # Maria paid $300 for the ticket
    hotel_cost = ticket_cost / 2  # Maria paid half of the ticket cost for the hotel
    total_cost = ticket_cost + hotel_cost  # Total cost of the trip
    initial_money = 760  # Maria had $760 at the beginning
    remaining_money = initial_money - total_cost  # Calculate the remaining money

    result = remaining_money
    return result

print(solution())