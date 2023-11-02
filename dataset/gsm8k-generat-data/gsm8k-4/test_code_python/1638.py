def solution():
    """It will take Richard and Sarah 3 years to save enough for a down payment on a house at their current rates. If the house's downpayment is $108000, calculate the amount each person saves per month if they share the monthly savings."""
    # Define the total down payment and the time to save it
    down_payment = 108000
    time_to_save = 3  # years

    # Calculate the total monthly savings required
    total_savings = down_payment / (time_to_save * 12)

    # Divide the total savings by 2 to get the monthly savings per person
    monthly_savings = total_savings / 2

    # return the result
    result = monthly_savings
    return result

print(solution())