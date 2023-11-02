def solution():
    total_amount = 100  # Gail's bills amount to $100
    num_5_bills = 4  # Gail has four $5 bills
    num_20_bills = 3  # Gail has three $20 bills

    # Calculate the total amount of Gail's $5 and $20 bills
    total_amount_known_bills = (num_5_bills * 5) + (num_20_bills * 20)

    # Calculate the total amount of Gail's $10 bills
    total_ten_bills = total_amount - total_amount_known_bills

    # Calculate the number of Gail's $10 bills
    num_10_bills = total_ten_bills / 10
    result = num_10_bills
    return result

print(solution())