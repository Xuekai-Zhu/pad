def solution():
    """Carl wants to buy a new coat that is quite expensive. He saved $25 each week for 6 weeks.  On the seventh week, he had to use a third of his saving to pay some bills. On the eighth week, his dad gave him some extra money for him to buy his dream coat. If the coat cost $170, how much money did his dad give him?"""
    # Calculate the total amount of money saved after 6 weeks
    total_saved = 25 * 6

    # Calculate the amount of money used to pay bills in the seventh week
    bills = total_saved / 3

    # Calculate the amount of money remaining after paying bills
    remaining = total_saved - bills

    # Calculate how much more money Carl needs to buy the coat
    shortfall = 170 - remaining

    # Calculate how much money Carl's dad gave him
    dad_money = shortfall

    # Display the amount of money Carl's dad gave him
    result = dad_money
    return result

print(solution())