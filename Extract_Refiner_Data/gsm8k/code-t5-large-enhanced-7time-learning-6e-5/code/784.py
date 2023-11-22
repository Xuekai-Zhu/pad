def solution():
    
    # Define the cost of the trip
    trip_cost = 300

    # Calculate the amount covered by help
    help_amount = trip_cost / 2

    # Calculate the total amount raised
    total_raised = 50 + help_amount

    # Calculate the amount missing
    missing_money = total_raised - trip_cost

    # Display the amount missing
    result = missing_money
    return result

print(solution())