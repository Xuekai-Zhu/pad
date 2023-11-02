def solution():
    """Uncle Bradley has a $1000 bill that he wants to change into smaller bills so he could give them to his nieces and nephews. He wants to change 3/10 of the money into $50 bills while the rest into $100 bills. How many pieces of bills will Uncle Bradley have in all?"""
    total_money = 1000
    fifty_bill_amount = total_money * 0.3 / 50
    hundred_bill_amount = (total_money - total_money * 0.3) / 100
    total_bills = fifty_bill_amount + hundred_bill_amount
    result = total_bills
    return result

print(solution())