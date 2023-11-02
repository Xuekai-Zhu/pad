def solution():
    """John sublets his apartment to 3 people who each pay $400 per month. He rents the apartment for $900 a month. How much profit does he make in a year?"""
    sublet_income = 400 * 3 * 12
    rental_income = 900 * 12
    expenses = 0
    profit = sublet_income + rental_income - expenses
    result = profit
    return result

print(solution())