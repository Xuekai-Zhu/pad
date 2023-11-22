def solution():
    
    # Define the initial amount in Katina's savings account
    initial_amount = 3000

    # Define the amount removed per month
    monthly_removal = 100

    # Calculate the total amount removed in 2 years
    total_removed = monthly_removal * 12 * 2

    # Calculate the remaining amount in Katina's savings account after 2 years
    remaining_amount = initial_amount - total_removed

    # Display the remaining amount in Katina's savings account after 2 years
    result = remaining_amount
    return result

print(solution())