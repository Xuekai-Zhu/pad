def solution():
    total_cds = 200  # Total number of CDs sold
    cds_at_10 = 0.4 * total_cds  # Number of CDs sold at $10
    cds_at_5 = 0.6 * total_cds  # Number of CDs sold at $5

    # Calculate the number of CDs bought by Prince at $10
    prince_cds_at_10 = 0.5 * cds_at_10

    # Calculate the amount spent by Prince on CDs sold at $10
    prince_amount_at_10 = prince_cds_at_10 * 10

    # Calculate the amount spent by Prince on CDs sold at $5
    prince_amount_at_5 = cds_at_5 * 5

    # Calculate the total amount spent by Prince
    total_amount = prince_amount_at_10 + prince_amount_at_5
    result = total_amount
    return result

print(solution())