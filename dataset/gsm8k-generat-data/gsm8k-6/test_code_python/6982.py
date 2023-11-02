def solution():
    # Calculate the cost per pound of mangoes
    cost_per_pound = 0.60 / 0.5  # Half a pound costs $0.60

    # Calculate how many pounds Kelly can buy with $12
    pounds_buyable = 12 / cost_per_pound

    result = pounds_buyable
    return result

print(solution())