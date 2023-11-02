def solution():
    
    # Define the cost of the bedroom set and the selling price of the old bedroom set
    bedroom_set_cost = 3000
    old_bedroom_price = 1000

    # Calculate the total cost of the bedroom set
    total_cost = bedroom_set_cost - old_bedroom_price

    # Calculate the amount to be paid per month
    monthly_payment = total_cost * 0.1

    # Display the monthly payment
    result = monthly_payment
    return result

print(solution())