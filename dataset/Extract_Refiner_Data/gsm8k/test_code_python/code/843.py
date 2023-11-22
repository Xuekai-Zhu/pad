def solution():
    
    # Define the initial investment amount and interest rate
    initial_amount = 300
    interest_rate = 0.75

    # Calculate the interest earned after 3 years
    interest_earned = initial_amount * interest_rate * 3

    # Calculate the total amount after 3 years
    total_amount = initial_amount + interest_earned

    # Display the total amount
    result = total_amount
    return result

print(solution())