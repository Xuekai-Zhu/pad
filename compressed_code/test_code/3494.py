def solution():
    
    total_money = 1000
    fifty_bill_amount = total_money * 0.3 / 50
    hundred_bill_amount = (total_money - total_money * 0.3) / 100
    total_bills = fifty_bill_amount + hundred_bill_amount
    result = total_bills
    return result

print(solution())