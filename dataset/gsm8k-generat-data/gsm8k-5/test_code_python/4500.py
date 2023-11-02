def solution():
    total_money = 1000  # Uncle Bradley has a $1000 bill
    money_for_50s = 3/10 * total_money  # 3/10 of the money will be changed into $50 bills
    money_for_100s = total_money - money_for_50s  # The rest of the money will be changed into $100 bills

    # Calculate the number of $50 bills Uncle Bradley will get
    num_50_bills = money_for_50s / 50

    # Calculate the number of $100 bills Uncle Bradley will get
    num_100_bills = money_for_100s / 100

    # Calculate the total number of bills Uncle Bradley will have in all
    total_bills = num_50_bills + num_100_bills
    result = total_bills
    return result

print(solution())