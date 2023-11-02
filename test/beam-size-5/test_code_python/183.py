def solution():
    
    # Define the initial amount owed to Benedict
    initial_amount = 100

    # Calculate the monthly interest amount
    monthly_interest = initial_amount * 0.02

    # Calculate the total amount owed after 3 months
    total_amount = initial_amount + (monthly_interest * 3)

    # Display the total amount owed to Benedict
    result = total_amount
    return result

print(solution())