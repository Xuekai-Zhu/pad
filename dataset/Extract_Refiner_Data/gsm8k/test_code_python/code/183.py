def solution():
    
    # Define the initial amount owedict and the interest rate
    initial_amount = 100
    interest_rate = 0.02

    # Calculate the interest earned after 3 months
    interest_earned = initial_amount * interest_rate * 3

    # Calculate the total amount owedict after 3 months
    total_amount_owedict = initial_amount + interest_earned

    # return the result
    result = total_amount_owedict
    return result

print(solution())