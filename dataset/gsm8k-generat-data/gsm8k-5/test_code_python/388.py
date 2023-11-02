def solution():
    rent_per_month = 900  # John rents the apartment for $900 a month
    sublet_price_per_person = 400  # John sublets the apartment to 3 people who each pay $400 per month
    sublet_income_per_month = sublet_price_per_person * 3  # John earns $400 per person from subletting
    total_income_per_month = rent_per_month + sublet_income_per_month  # John's total monthly income
    annual_income = total_income_per_month * 12  # John's annual income

    # Calculate John's profit for the year
    expenses = rent_per_month * 12  # John pays $900 per month for the apartment, for 12 months
    profit = annual_income - expenses
    result = profit
    return result

print(solution())