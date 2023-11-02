def solution():
    roses_last_year = 12  # Kyle picked a dozen roses last year
    roses_this_year = roses_last_year / 2  # Kyle picked half the number of roses this year
    total_roses = 2 * roses_last_year  # Kyle wants to give his mother twice as many roses as last year
    roses_needed = total_roses - roses_this_year  # Kyle needs to buy the remaining number of roses
    cost_per_rose = 3  # The grocery store sells one rose for $3

    # Calculate the total cost of the roses Kyle needs to buy
    total_cost = roses_needed * cost_per_rose
    result = total_cost
    return result

print(solution())