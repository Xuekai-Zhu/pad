def solution():
    # Calculate the amount of money Mandy and Manny have in total
    mandy_money = 3 * 20  # Mandy has three $20 bills
    manny_money = 2 * 50  # Manny has two $50 bills
    total_money = mandy_money + manny_money

    # Calculate the number of $10 bills they receive after exchanging their bills
    num_10_bills = total_money // 10

    # Calculate how many more $10 bills Manny will have than Mandy
    mandy_10_bills = mandy_money // 10
    manny_10_bills = manny_money // 10
    diff_10_bills = manny_10_bills - mandy_10_bills

    result = diff_10_bills
    return result

print(solution())