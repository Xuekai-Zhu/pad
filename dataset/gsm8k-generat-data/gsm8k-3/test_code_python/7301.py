def solution():
    """Holly gets 26 paychecks per year.  If she puts $100.00 from every paycheck into her 401K, her company will match that contribution by 6%.  How much money has she and her company contributed to her 401k after 1 year?"""
    # Define the number of paychecks Holly gets per year and the amount she contributes per paycheck
    PAYCHECKS_PER_YEAR = 26
    HOLLY_CONTRIBUTION = 100

    # Calculate Holly's contribution to her 401k for 1 year
    holly_total_contribution = HOLLY_CONTRIBUTION * PAYCHECKS_PER_YEAR

    # Calculate Holly's company's contribution to her 401k for 1 year
    company_contribution = holly_total_contribution * 0.06

    # Calculate the total contribution to Holly's 401k for 1 year
    total_contribution = holly_total_contribution + company_contribution

    # Display the total contribution to Holly's 401k for 1 year
    result = total_contribution
    return result

print(solution())