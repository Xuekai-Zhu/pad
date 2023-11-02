def solution():
    # Define the cost of each sandwich and the number ordered
    sandwich_cost = 5
    num_sandwiches = 18

    # Calculate the total cost of the sandwiches
    total_sandwich_cost = sandwich_cost * num_sandwiches

    # Calculate the tip amount
    tip_percent = 0.1
    tip_amount = total_sandwich_cost * tip_percent

    # Add the delivery fee, sandwich cost, and tip to get the total payment
    total_payment = total_sandwich_cost + 20 + tip_amount
    result = total_payment
    return result

print(solution())