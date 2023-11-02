def solution():
    """Aaron and his brother Carson each saved up $40 to go to dinner. The bill is 3/4 of their total money. After, they go out for ice cream. Each scoop costs $1.5 and they get the same amount as each other. If they leave with $1 in change each, how many scoops did they each buy?"""
    total_money = 80
    dinner_cost = total_money * 3/4
    remaining_money = total_money - dinner_cost - 2  # minus 2 for the dollar each they have in change
    cost_per_scoop = 1.5
    num_scoops_each = remaining_money / (cost_per_scoop * 2)  # divide by 2 since they each get the same amount
    result = num_scoops_each
    return result

print(solution())