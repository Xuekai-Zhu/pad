def solution():
    """Jenny collects cans and bottles to take down to the recycling center. Each bottle weighs 6 ounces and each can weighs 2 ounces. Jenny can carry a total of 100 ounces. She collects 20 cans and as many bottles as she can carry. If she gets paid 10 cents per bottle and 3 cents per can, how much money does she make (in cents)?"""
    can_weight = 2
    bottle_weight = 6
    max_weight = 100
    total_weight = 20 * can_weight
    bottles = (max_weight - total_weight) // bottle_weight
    money_made = (bottles * 10) + (20 * 3)
    result = money_made
    return result

print(solution())