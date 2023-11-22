def solution():
    
    # Define the cost of renting the theater and the additional guests
    RENT_COST = 125 + 6*7 + 6*6

    # Calculate the total cost of the party
    total_cost = RENT_COST + RENT_COST + (20+7+6) + 13

    # Display the total cost
    result = total_cost
    return result

print(solution())