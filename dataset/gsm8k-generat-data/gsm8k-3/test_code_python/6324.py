def solution():
    """Jack collects all his neighbors' recycling and sorts out the cans and bottles to return for the deposit. He gets 10 cents per bottle and 5 cents per can. If he recycled 80 bottles and made $15, how many cans did he recycle?"""
    # Define the payout per bottle and can
    BOTTLE_PAYOUT = 0.1
    CAN_PAYOUT = 0.05

    # Define the number of bottles and payout from bottles
    num_bottles = 80
    bottle_payout = num_bottles * BOTTLE_PAYOUT

    # Calculate the total payout
    total_payout = 15

    # Calculate the payout from cans
    can_payout = total_payout - bottle_payout

    # Calculate the number of cans
    num_cans = can_payout / CAN_PAYOUT

    # Display the number of cans
    result = num_cans
    return result

print(solution())