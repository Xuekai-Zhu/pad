def solution():
    """Archie received his medical receipt from his doctor, and he needs to take antibiotics three times a day. If antibiotic costs $3 each and he needs to take it for a week, how much money does he need to buy the antibiotics?"""
    # Define the cost of one antibiotic and the number of days Archie needs to take it
    antibiotic_cost = 3
    days = 7

    # Calculate the total cost of antibiotics for one day
    daily_cost = antibiotic_cost * 3

    # Calculate the total cost of antibiotics for the entire week
    total_cost = daily_cost * days

    # Return the result
    result = total_cost
    return result

print(solution())