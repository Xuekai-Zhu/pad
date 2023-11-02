def solution():
    
    # Define the cost of each cell phone and the number of phones purchased
    PHONE_COST = 150
    NUM_PHONES = 5

    # Calculate the total cost of the phones for 3 months
    total_cost = PHONE_COST * NUM_PHONES * 3

    # Calculate the interest rate
    interest_rate = 0.02

    # Calculate the interest earned for each unit
    interest_earned = total_cost * interest_rate

    # Calculate the total cost for 3 months
    total_cost_3_months = total_cost + interest_earned

    # Display the total cost for 3 months
    result = total_cost_3_months
    return result

print(solution())