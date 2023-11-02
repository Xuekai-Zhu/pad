def solution():
    """Luke pays a school fee. His mother gave him one $50 bill, two $20 bills, and three $10 bills. His father gave him four $50 bills, one $20 bill, and one $10 bill. If his parents gave him the exact amount for the school fee, how much is the school fee?"""
    # Define the amount of money Luke's mother gave him
    mother_money = 50 + 2*20 + 3*10

    # Define the amount of money Luke's father gave him
    father_money = 4*50 + 1*20 + 1*10

    # Calculate the total amount of money Luke has
    total_money = mother_money + father_money

    # The school fee is exactly the total amount of money Luke has
    school_fee = total_money

    result = school_fee
    return result

print(solution())