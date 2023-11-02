def solution():
    # Calculate the total amount of money Marly has
    total_money = (10 * 20) + (8 * 10) + (4 * 5)

    # Calculate the total number of $100 bills Marly can get
    num_hundred_bills = total_money // 100
    result = num_hundred_bills
    return result

print(solution())