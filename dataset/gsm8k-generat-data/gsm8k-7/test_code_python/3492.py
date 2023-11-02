def solution():
    # Amount of money Samuel has
    total_money = 150

    # Number of $10 bills Samuel has
    num_10_bills = 5

    # Total value of $10 bills Samuel has
    total_10_bills = num_10_bills * 10

    # Total value of $20 bills Samuel has
    total_20_bills = 4 * 20

    # Total value of $5 bills Samuel has
    total_5_bills = total_money - total_10_bills - total_20_bills

    # Number of $5 bills Samuel has
    num_5_bills = total_5_bills / 5

    # Total number of bills Samuel has
    total_bills = num_5_bills + num_10_bills + 4

    result = total_bills
    return result

print(solution())