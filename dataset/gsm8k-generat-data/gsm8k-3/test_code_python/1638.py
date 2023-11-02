def solution():
    """It will take Richard and Sarah 3 years to save enough for a down payment on a house at their current rates.
    If the house's downpayment is $108000, calculate the amount each person saves per month if they share the monthly savings."""
    #Calculate the total number of months they will take to save enough for the down payment.
    total_months = 3 * 12

    #Calculate the total amount they need to save each month.
    monthly_savings = 108000 / total_months

    #Calculate the amount each person needs to save per month if they share the monthly savings.
    per_person_savings = monthly_savings / 2

    result = per_person_savings
    return result

print(solution())