def solution():
    """Daria just got a new credit card so she could buy some furniture. Daria has $500 saved ready to pay for the furniture she buys, but the rest of the money will have to stay on her credit card statement until the next month, when she can pay it off with interest. She bought a couch for $750, a table for $100 and a lamp for $50. After she pays the initial $500, how much does she still owe before interest?"""
    # Define the total cost of the furniture
    total_cost = 750 + 100 + 50

    # Subtract Daria's savings from the total cost to get the amount charged to her credit card
    charged_amount = total_cost - 500

    # Display the amount Daria still owes before interest
    result = charged_amount
    return result

print(solution())