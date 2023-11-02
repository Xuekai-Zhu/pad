def solution():
    monthly_rate = 50  # monthly internet rate
    discounted_rate = monthly_rate * 0.95  # discounted rate if customer pays before 25th of the month
    total_cost = monthly_rate * 4  # total cost if customer pays on 25th of each month
    cost_with_discount = discounted_rate * 4  # total cost with 5% discount if customer pays before 25th of each month

    # Calculate the final amount paid by the customer for 4 months
    if datetime.datetime.now().day < 25:
        final_cost = cost_with_discount + (total_cost - cost_with_discount)
    else:
        final_cost = total_cost
    result = final_cost
    return result

print(solution())