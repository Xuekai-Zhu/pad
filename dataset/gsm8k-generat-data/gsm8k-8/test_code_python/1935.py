def solution():
    # Define the amount she had in her savings account initially
    total_savings = 0

    # Calculate the initial amount by working backward from the current amount
    current_amount = 2900
    current_amount += 1500 # Add April expenses
    current_amount /= 0.6 # Divide by remaining savings percentage (40%)
    total_savings = current_amount

    # Return the amount she had in her savings initially
    return total_savings

print(solution())