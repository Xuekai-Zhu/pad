def solution():
    steak_and_eggs = 16
    chicken_fried_steak = 14
    tip_percentage = 20
    total_bill = steak_and_eggs + chicken_fried_steak
    tip_amount = total_bill * (tip_percentage / 100)
    bill_without_tip = total_bill + tip_amount
    half_bill = bill_without_tip / 2
    result = half_bill + tip_amount
    return result

print(solution())