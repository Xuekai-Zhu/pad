def solution():
    rows_planted = 0
    for kid in range(4):
        # Calculate the number of rows each kid planted
        rows_planted += (kid + 1) * 5  # Each kid planted 5 more rows than the previous kid
        # Calculate the number of ears of corn each kid planted
        ears_planted = rows_planted * 70
        # Calculate the number of seed bags each kid used
        seed_bags = ears_planted * 2 / 48
        # Calculate the amount of money each kid earned
        money_earned = rows_planted * 1.5
        # Calculate the amount of money each kid spent on dinner
        money_spent = money_earned / 2 - 36
        # Calculate the remaining amount of money each kid has
        money_remaining = money_earned / 2 - money_spent
        # Calculate the number of seed bags each kid used with the remaining money
        seed_bags_remaining = money_remaining / 1.5 / 2
        # Update the total seed bags used by all kids
        seed_bags += seed_bags_remaining

    result = seed_bags / 4  # Divide the total seed bags by 4 to get the number used by each kid
    return result

print(solution())