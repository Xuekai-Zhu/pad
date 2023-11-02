def solution():
    bill_total = 26
    tip_percentage = 5
    tip_amount = bill_total * (tip_percentage / 100)
    good_tip_percentage = 20
    good_tip_amount = bill_total * (good_tip_percentage / 100)
    difference = good_tip_amount - tip_amount
    result = difference
    
    return result

print(solution())