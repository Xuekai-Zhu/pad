def solution():
    """Sam shared a sum of money between his three cousins Sandra, Amy and Ruth in the ratio 2:1:3 respectively. If Amy got $50, how much did Sandra get?"""
    # Define the ratio of sharing
    sandra_ratio = 2
    amy_ratio = 1
    ruth_ratio = 3

    # Define the amount of money Amy got
    amy_money = 50

    # Calculate the total ratio
    total_ratio = sandra_ratio + amy_ratio + ruth_ratio

    # Calculate the ratio multiplier
    amy_multiplier = amy_ratio / total_ratio

    # Calculate the amount of money shared between the three cousins
    total_money = amy_money / amy_multiplier

    # Calculate the amount of money Sandra got
    sandra_money = sandra_ratio / total_ratio * total_money

    # Return the result
    result = sandra_money
    return result

print(solution())