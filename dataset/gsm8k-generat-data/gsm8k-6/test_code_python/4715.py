def solution():
    # Calculate the weekly cost for trash and recycling
    weekly_cost = 2*10 + 5  # $10 per trash bin, $5 per recycling bin

    # Calculate the total cost for the month
    total_cost = weekly_cost * 4 

    # Apply the 18% discount
    total_cost *= 0.82  

    # Add the $20 fine for inappropriate items in recycling bin
    total_cost += 20  

    result = total_cost
    return result

print(solution())