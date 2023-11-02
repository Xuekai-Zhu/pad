def solution():
    """Carl wants to buy a new coat that is quite expensive. He saved $25 each week for 6 weeks. On the seventh week, he had to use a third of his saving to pay some bills. On the eighth week, his dad gave him some extra money for him to buy his dream coat. If the coat cost $170, how much money did his dad give him?"""
    # Calculate the total savings after 6 weeks
    total_savings = 25 * 6

    # Calculate the amount of money Carl used to pay bills
    bills_payment = total_savings / 3

    # Calculate the remaining savings after paying bills
    remaining_savings = total_savings - bills_payment

    # Calculate the amount of money Carl still needs to buy the coat
    coat_cost = 170
    remaining_money = coat_cost - remaining_savings

    # Calculate the amount of money Carl's dad gave him
    dad_money = remaining_money

    result = dad_money
    return result

print(solution())