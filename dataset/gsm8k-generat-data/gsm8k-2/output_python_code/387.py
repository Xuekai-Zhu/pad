def solution():
    """John sublets his apartment to 3 people who each pay $400 per month. He rents the apartment for $900 a month. How much profit does he make in a year?"""
    rent_income = 900 * 12
    sublet_income = 400 * 3 * 12
    total_income = rent_income + sublet_income
    expenses = rent_income / 2  # assuming half the rent goes to expenses
    profit = total_income - expenses
    result = profit
    return result

print(solution())