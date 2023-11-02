def solution():
    """Jenny collects cans and bottles to take down to the recycling center. Each bottle weighs 6 ounces and each can weighs 2 ounces. Jenny can carry a total of 100 ounces. She collects 20 cans and as many bottles as she can carry. If she gets paid 10 cents per bottle and 3 cents per can, how much money does she make (in cents)?"""
    
    # Define the weight of a bottle and a can
    bottle_weight = 6
    can_weight = 2

    # Define the total weight that Jenny can carry
    total_weight = 100

    # Calculate the number of bottles that Jenny can carry
    max_bottles = (total_weight - can_weight*20) // bottle_weight

    # Calculate the total number of cents that Jenny makes from the cans
    can_money = 3 * 20

    # Calculate the total number of cents that Jenny makes from the bottles
    bottle_money = 10 * max_bottles

    # Calculate the total money that Jenny makes
    total_money = can_money + bottle_money

    result = total_money
    return result

print(solution())