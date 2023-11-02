def solution():
    """Luke pays a school fee. His mother gave him one $50 bill, two $20 bills, and three $10 bills. His father gave him four $50 bills, one $20 bill, and one $10 bill. If his parents gave him the exact amount for the school fee, how much is the school fee?"""
    mother_money = (1*50) + (2*20) + (3*10)
    father_money = (4*50) + (1*20) + (1*10)
    total_money = mother_money + father_money
    result = total_money
    return result

print(solution())