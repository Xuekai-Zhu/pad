def solution():
    
    initial_bill = 40
    delivery_fee = 0.25 * initial_bill
    tip = 4
    final_bill = initial_bill + delivery_fee + tip
    result = final_bill
    return result

print(solution())