def solution():
    """It will take Richard and Sarah 3 years to save enough for a down payment on a house at their current rates. If the house's downpayment is $108000, calculate the amount each person saves per month if they share the monthly savings."""
    years_to_save = 3
    total_amount = 108000
    months_to_save = years_to_save * 12
    total_savings_per_month = total_amount / months_to_save
    savings_per_person_per_month = total_savings_per_month / 2
    result = savings_per_person_per_month
    return result

print(solution())