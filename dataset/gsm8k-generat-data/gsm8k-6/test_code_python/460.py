def solution():
    # Calculate the percentage of bonus
    bonus_percentage = (10000 / 100000) * 100  # last year's bonus as a percentage of his salary

    # Calculate this year's bonus based on the bonus percentage
    this_year_bonus = (bonus_percentage / 100) * 200000

    # Calculate John's total income
    total_income = 200000 + this_year_bonus

    result = total_income
    return result

print(solution())