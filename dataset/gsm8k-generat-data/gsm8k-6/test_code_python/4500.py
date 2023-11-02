def solution():
    # Determine how much money will be changed into $50 bills and $100 bills
    money_50_bills = (3/10) * 1000  # 3/10 of the money will be changed into $50 bills
    money_100_bills = 1000 - money_50_bills  # rest of the money will be changed into $100 bills

    # Determine the number of $50 bills and $100 bills
    num_50_bills = money_50_bills / 50  # each $50 bill is worth $50
    num_100_bills = money_100_bills / 100  # each $100 bill is worth $100

    # Calculate the total number of bills
    total_bills = num_50_bills + num_100_bills

    result = int(total_bills)
    return result

print(solution())