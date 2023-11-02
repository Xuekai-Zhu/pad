def solution():
    """Maria went on a trip to Belgium. She paid $300 for the ticket and half of that for the hotel. How much money does she have left, when she had $760 at the beginning?"""
    initial_money = 760
    ticket_cost = 300
    hotel_cost = ticket_cost / 2
    remaining_money = initial_money - ticket_cost - hotel_cost
    result = remaining_money
    return result

print(solution())