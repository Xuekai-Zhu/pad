def solution():
    borrowed_money = 1200
    interest_rate = 10
    interest_amount = borrowed_money * (interest_rate / 100)
    total_to_pay_back = borrowed_money + interest_amount
    result = total_to_pay_back
    return result

print(solution())