def solution():
    # Define the starting amount
    starting_amount = 80
    
    # Calculate Monday's spending
    monday_spending = starting_amount / 2
    amount_left = starting_amount - monday_spending
    
    # Calculate Tuesday's spending
    tuesday_spending = amount_left / 5
    amount_left = amount_left - tuesday_spending
    
    # Calculate Wednesday's spending
    wednesday_spending = (3/8) * amount_left
    amount_left = amount_left - wednesday_spending
    
    result = amount_left
    return result

print(solution())