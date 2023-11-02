def solution():
    # Calculate the total cost of buying the dozen boxes
    cost_of_boxes = 10 * 12  # $10 per box, 12 boxes in total

    # Calculate the profit from selling the packages of six highlighters each
    num_packages = 5  # five boxes rearranged into packages of 6 highlighters each
    highlighters_in_packages = num_packages * 6  # 6 highlighters in each package
    revenue_from_packages = highlighters_in_packages * 3  # $3 per package
    cost_of_packages = num_packages * 10  # $10 cost of each box rearranged into packages
    profit_from_packages = revenue_from_packages - cost_of_packages

    # Calculate the profit from selling the remaining highlighters separately
    num_highlighters_remaining = (12 * 30) - highlighters_in_packages  # total number of highlighters remaining
    num_packs_of_three = num_highlighters_remaining // 3  # number of packs of three highlighters 
    revenue_from_remaining = num_packs_of_three * 2  # $2 revenue for each pack of three highlighters
    cost_of_remaining = (12 - num_packages) * 10  # $10 cost of each box remaining
    profit_from_remaining = revenue_from_remaining - cost_of_remaining

    # Calculate the total profit
    total_profit = profit_from_packages + profit_from_remaining
    result = total_profit
    return result

print(solution())