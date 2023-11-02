def solution():
    """Uncle Bradley has a $1000 bill that he wants to change into smaller bills so he could give them to his nieces and nephews. He wants to change 3/10 of the money into $50 bills while the rest into $100 bills. How many pieces of bills will Uncle Bradley have in all?"""
    total_money = 1000
    percentage_for_50s = 0.3
    percentage_for_100s = 0.7
    money_for_50s = total_money * percentage_for_50s
    money_for_100s = total_money * percentage_for_100s
    num_50s = money_for_50s / 50
    num_100s = money_for_100s / 100
    total_bills = num_50s + num_100s
    result = total_bills
    return result

print(solution())