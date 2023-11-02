def solution():
    num_100_bills = 2
    num_50_bills = 5
    num_10_bills = 10

    # Calculate the total amount of money in the $100 bills
    total_100_bills = num_100_bills * 100

    # Calculate the total amount of money in the $50 bills
    total_50_bills = num_50_bills * 50

    # Calculate the total amount of money in the $10 bills
    total_10_bills = num_10_bills * 10

    # Calculate the total amount of money Meghan had
    total_money = total_100_bills + total_50_bills + total_10_bills
    result = total_money
    return result

print(solution())