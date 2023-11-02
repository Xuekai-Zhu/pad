def solution():
    """Kathryn moved to a new city for the new job she had landed two weeks ago. Her rent was $1200, 1/2 of what she spent on food and travel expenses in a month. Luckily, she found a new friend Shelby, who moved in with her to share the rent. If her salary was $5000 per month, how much money remained after her expenses?"""
    rent_per_month = 1200
    shared_rent = rent_per_month / 2
    total_expenses = rent_per_month + (2 * shared_rent)
    food_travel_expenses = total_expenses - rent_per_month
    salary = 5000
    money_remaining = salary - total_expenses
    result = money_remaining
    return result

print(solution())