def solution():
    """Maria went on a trip to Belgium. She paid $300 for the ticket and half of that for the hotel. How much money does she have left, when she had $760 at the beginning? """
    # Define the cost of the ticket and hotel
    ticket_cost = 300
    hotel_cost = ticket_cost / 2

    # Define Maria's initial budget
    initial_budget = 760

    # Calculate Maria's total expenses
    total_expenses = ticket_cost + hotel_cost

    # Calculate Maria's remaining budget
    remaining_budget = initial_budget - total_expenses

    # Display Maria's remaining budget
    result = remaining_budget
    return result

print(solution())