def solution():
    total_money = 150  # The total amount of money in Samuel's wallet is $150
    num_10_bills = 5  # Samuel has $50 worth of $10-bills, so he has 5 of them
    num_20_bills = 4  # Samuel has 4 $20-bills

    # Calculate the number of $5-bills
    num_5_bills = (total_money - (num_10_bills * 10) - (num_20_bills * 20)) / 5

    # Calculate the total number of bills
    total_bills = num_5_bills + num_10_bills + num_20_bills
    result = total_bills
    return result

print(solution())