def solution():
    mandy_money = 3 * 20  # Mandy has three $20 bills
    manny_money = 2 * 50  # Manny has two $50 bills

    # Calculate the total amount of money they have
    total_money = mandy_money + manny_money

    # Calculate the number of $10 bills they will receive after exchanging their money
    num_10_bills = total_money // 10

    # Calculate how many more $10 bills Manny will have than Mandy
    difference = (num_10_bills - (mandy_money // 10)) - (mannt_money // 10)
    result = difference
    return result

print(solution())