def solution():
    candy_bar_cost = 0.50  # Carl spends $0.50 on each candy bar
    neighbor_payment = 0.75  # Carl earns $0.75 for taking out his neighbor's trash each week
    weeks = 4  # Carl wants to know how many candy bars he can buy in 4 weeks

    # Calculate the total amount of money Carl earns in 4 weeks
    total_earnings = neighbor_payment * weeks

    # Calculate the number of candy bars Carl can buy with his earnings
    candy_bars = total_earnings / candy_bar_cost
    result = candy_bars
    return result

print(solution())