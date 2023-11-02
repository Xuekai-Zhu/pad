def solution():
    # Calculate the total amount of money saved by Carl in 6 weeks
    total_savings = 25 * 6

    # Calculate the amount of money left after paying the bills in the 7th week
    left_savings = total_savings - (1/3 * total_savings)

    # Calculate the remaining amount of money needed to buy the coat
    remaining_money = 170 - left_savings

    # Calculate the amount of money Carl's dad gave him
    dad_money = remaining_money

    result = dad_money
    return result

print(solution())