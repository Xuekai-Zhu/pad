def solution():
    """It will take Richard and Sarah 3 years to save enough for a down payment on a house at their current rates. If the house's downpayment is $108000, calculate the amount each person saves per month if they share the monthly savings."""
    down_payment = 108000
    savings_time = 3  # in years
    total_savings = down_payment / savings_time
    monthly_savings = total_savings / 12
    amount_per_person = monthly_savings / 2
    result = amount_per_person
    return result

print(solution())