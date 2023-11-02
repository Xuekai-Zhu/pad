def solution():
    cost_per_dozen = 5  # Rolls cost 5 dollars per dozen
    total_cost = 15  # John spent 15 dollars
    dozens_purchased = total_cost / cost_per_dozen  # Calculate how many dozens John purchased

    # Calculate how many rolls John purchased
    rolls_purchased = dozens_purchased * 12
    result = rolls_purchased
    return result

print(solution())