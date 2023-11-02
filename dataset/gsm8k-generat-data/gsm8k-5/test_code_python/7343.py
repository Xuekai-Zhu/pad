def solution():
    total_money = 32  # Tamara made $32 from the brownies
    pans_of_brownies = 2  # Tamara made 2 pans of brownies
    num_of_brownies = pans_of_brownies * 8  # Each pan has 8 pieces or brownies

    # Calculate the cost of each brownie
    cost_per_brownie = total_money / num_of_brownies
    result = cost_per_brownie
    return result

print(solution())