def solution():
    # Calculate the total revenue from haircuts
    revenue_haircuts = 30 * 4

    # Calculate the total revenue from perms
    revenue_perms = 40 * 1

    # Calculate the total revenue from dye jobs
    revenue_dyejobs = (60 * 2) - 10  # Subtract the cost of the hair dye

    # Calculate the total revenue for the day
    total_revenue = revenue_haircuts + revenue_perms + revenue_dyejobs

    # Add the tips to the total revenue
    total_revenue += 50

    result = total_revenue
    return result

print(solution())