def solution():
    """Aaron and his brother Carson each saved up $40 to go to dinner. The bill is 3/4 of their total money. After, they go out for ice cream. Each scoop costs $1.5 and they get the same amount as each other. If they leave with $1 in change each, how many scoops did they each buy?"""
    # Define the amount of money Aaron and Carson have
    total_money = 40 * 2

    # Calculate the total amount of money spent on dinner
    dinner_cost = total_money * (3/4)

    # Calculate the amount of money left for ice cream
    ice_cream_money = total_money - dinner_cost - 2

    # Calculate the number of scoops they each bought
    scoops_each = int(ice_cream_money / (2 * 1.5))

    # Return the result
    result = scoops_each
    return result

print(solution())