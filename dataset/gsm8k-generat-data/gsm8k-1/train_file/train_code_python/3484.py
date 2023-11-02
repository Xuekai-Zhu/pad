def solution():
    """Maria went on a trip to Belgium. She paid $300 for the ticket and half of that for the hotel. How much money does she have left, when she had $760 at the beginning?"""
    initial_money = 760
    ticket_price = 300
    hotel_price = ticket_price / 2
    total_expenses = ticket_price + hotel_price
    remaining_money = initial_money - total_expenses
    result = remaining_money
    return result

print(solution())