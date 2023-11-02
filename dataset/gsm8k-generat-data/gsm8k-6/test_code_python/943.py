def solution():
    # Calculate the cost and revenue per dozen donuts
    cost_per_dozen = 2.4
    revenue_per_dozen = 12  # selling 12 individual donuts for $1 each yields $12 in revenue

    # Calculate the number of dozens needed to reach the fundraising goal
    dozens_needed = 96 / (revenue_per_dozen - cost_per_dozen)
    result = dozens_needed
    return result

print(solution())