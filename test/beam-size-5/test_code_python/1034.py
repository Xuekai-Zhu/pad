def solution():
    loans_per_year = 50000  # Jim gets $50,000 in loans per year
    years_to_finish = 4  # Jim has 4 years to finish
    income_per_year = loans_per_year * years_to_finish  # Jim gets $50,000 in loans per year
    years_to_college = income_per_year - 25  # Jim had a 25k a year job before college
    years_to_earn = years_to_college * years_to_college  # Calculate the number of years it would take Jim to earn the money equivalent to the loans

    result = years_to_earn
    return result

print(solution())