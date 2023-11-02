def solution():
    # Define the number of $10 bills and calculate the number of $5 bills
    num_10_bills = 10
    num_5_bills = num_10_bills - 4

    # Calculate the total amount of money
    total_money = num_10_bills * 10 + num_5_bills * 5
    result = total_money
    return result

print(solution())