def solution():
    # Calculate the total revenue from haircuts
    revenue_haircuts = 30 * 4

    # Calculate the total revenue from perms
    revenue_perms = 40 * 1

    # Calculate the total revenue from dye jobs
    revenue_dye_jobs = (60 - 10) * 2 # subtract the cost of hair dye from the price of dye jobs

    # Calculate the total revenue for the day
    total_revenue = revenue_haircuts + revenue_perms + revenue_dye_jobs + 50  # add tips to the total revenue

    result = total_revenue
    return result

print(solution())