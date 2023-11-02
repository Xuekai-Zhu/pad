def solution():
    """Maria went on a trip to Belgium. She paid $300 for the ticket and half of that for the hotel. How much money does she have left, when she had $760 at the beginning?"""
    # Define the initial amount of money Maria had
    initial_amount = 760

    # Calculate the amount Maria spent on the ticket
    ticket_cost = 300

    # Calculate the amount Maria spent on the hotel
    hotel_cost = ticket_cost / 2

    # Calculate the total amount of money Maria spent on the trip
    total_cost = ticket_cost + hotel_cost

    # Calculate the amount of money Maria has left after the trip
    remaining_amount = initial_amount - total_cost

    # return the result
    result = remaining_amount
    return result

print(solution())