def solution():
    num_10_bills = 10
    num_5_bills = num_10_bills - 4

    # Calculate the total amount of money from the $10 bills
    total_10_bills = num_10_bills * 10

    # Calculate the total amount of money from the $5 bills
    total_5_bills = num_5_bills * 5

    # Calculate the total amount of money Shelly has in all
    total_money = total_10_bills + total_5_bills
    result = total_money
    return result

print(solution())