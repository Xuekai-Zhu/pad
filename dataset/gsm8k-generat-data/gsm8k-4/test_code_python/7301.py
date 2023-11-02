def solution():
    """Holly gets 26 paychecks per year. If she puts $100.00 from every paycheck into her 401K, her company will match that contribution by 6%. How much money has she and her company contributed to her 401k after 1 year?"""
    # Define the variables
    paychecks_per_year = 26
    contribution_per_paycheck = 100
    company_match_percentage = 0.06

    # Calculate Holly's annual contribution
    holly_contribution = paychecks_per_year * contribution_per_paycheck

    # Calculate the company's matching contribution
    company_match = holly_contribution * company_match_percentage

    # Calculate the total contribution after 1 year
    total_contribution = holly_contribution + company_match

    # Return the result
    result = total_contribution
    return result

print(solution())