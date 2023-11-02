def solution():
    paycheck_amount = 100.00
    paychecks_per_year = 26
    company_match = 0.06

    # Calculate the total amount contributed by Holly and her company in one year
    total_contributed = paycheck_amount * paychecks_per_year * (1 + company_match)
    result = total_contributed
    return result

print(solution())