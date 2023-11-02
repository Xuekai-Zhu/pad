def solution():
    num_paychecks = 26  # Holly gets 26 paychecks per year
    personal_contribution = 100.00  # Holly puts $100.00 from every paycheck into her 401K
    company_match = 0.06 * personal_contribution  # Holly's company will match her contribution by 6%

    # Calculate the total contribution from Holly and her company after 1 year
    total_contribution = num_paychecks * (personal_contribution + company_match)

    result = total_contribution
    return result

print(solution())