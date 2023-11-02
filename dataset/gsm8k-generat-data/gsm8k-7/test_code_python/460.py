def solution():
    last_year_pay = 100000
    last_year_bonus = 10000
    this_year_pay = 200000

    # Determine the percentage increase in pay from last year to this year
    percent_increase = (this_year_pay - last_year_pay) / last_year_pay

    # Calculate the bonus for this year based on the same percentage increase
    this_year_bonus = last_year_bonus * (1 + percent_increase)

    # Calculate John's total income for this year
    total_income = this_year_pay + this_year_bonus
    result = total_income
    return result

print(solution())