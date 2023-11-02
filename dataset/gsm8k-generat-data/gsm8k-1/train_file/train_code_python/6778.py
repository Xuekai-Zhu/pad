def solution():
    """Mandy has three $20 bills while Manny has two $50 bills. If both of them decide to exchange their bills for $10 bills, how many more $10 bills than Mandy will Manny have?"""
    mandy_money = 3 * 20
    manny_money = 2 * 50
    total_money = mandy_money + manny_money
    exchanged_money = total_money // 10
    mandy_bills = mandy_money // 10
    manny_bills = manny_money // 10
    manny_exchanged_bills = (exchanged_money - mandy_bills) - manny_bills
    result = manny_exchanged_bills
    return result

print(solution())