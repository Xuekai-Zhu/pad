def solution():
    """Jim decides to go to college to earn some more money. It takes him 4 years to finish and he gets $50,000 in loans per year. If he had a 25k a year job before college and his college degree tripled his income, how long would it take to earn the money equivalent to the loans and the money lost from not working while in school."""
    years_in_college = 4
    loan_amount = 50000
    lost_income = 25000
    new_income = 3 * lost_income
    total_lost_income = lost_income * years_in_college
    total_loans = loan_amount * years_in_college
    total_cost = total_loans + total_lost_income
    time_to_earn = total_cost / (new_income - lost_income)
    result = time_to_earn
    return result

print(solution())