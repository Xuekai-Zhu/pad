def solution():
    total_money = 1000
    ratio_of_fifty_bills = 3/10

    # Calculate the amount of money to be changed into $50 bills
    money_for_fifty_bills = total_money * ratio_of_fifty_bills

    # Calculate the number of $50 bills to be received
    num_fifty_bills = money_for_fifty_bills / 50

    # Calculate the amount of money to be changed into $100 bills
    money_for_hundred_bills = total_money - money_for_fifty_bills

    # Calculate the number of $100 bills to be received
    num_hundred_bills = money_for_hundred_bills / 100

    # Calculate the total number of bills
    total_num_bills = num_fifty_bills + num_hundred_bills
    result = total_num_bills
    return result

print(solution())