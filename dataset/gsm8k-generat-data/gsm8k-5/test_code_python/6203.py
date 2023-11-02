def solution():
    cost_of_7_spoons = 21  # A set of 7 spoons costs $21

    # Calculate the cost of one spoon in the set
    cost_of_one_spoon = cost_of_7_spoons / 7

    # Calculate the cost of 5 spoons if each spoon is sold separately
    cost_of_5_spoons = cost_of_one_spoon * 5
    result = cost_of_5_spoons
    return result

print(solution())