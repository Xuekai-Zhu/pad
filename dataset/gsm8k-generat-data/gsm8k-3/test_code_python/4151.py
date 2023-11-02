def solution():
    """Jenny collects cans and bottles to take down to the recycling center. Each bottle weighs 6 ounces and each can weighs 2 ounces. Jenny can carry a total of 100 ounces. She collects 20 cans and as many bottles as she can carry. If she gets paid 10 cents per bottle and 3 cents per can, how much money does she make (in cents)?"""
    # Define the weight of each bottle and can
    BOTTLE_WEIGHT = 6
    CAN_WEIGHT = 2

    # Define the maximum weight Jenny can carry and the number of cans she collects
    MAX_WEIGHT = 100
    can_count = 20

    # Calculate the number of bottles she can carry
    bottle_count = int((MAX_WEIGHT - (CAN_WEIGHT * can_count)) / BOTTLE_WEIGHT)

    # Calculate the total earnings
    total_earnings = (bottle_count * 10) + (can_count * 3)

    # Display the total earnings
    result = total_earnings
    return result

print(solution())