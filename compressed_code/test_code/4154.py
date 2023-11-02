def solution():
    
    bill = 26
    bad_tip = 0.05 * bill
    good_tip = 0.20 * bill
    difference = good_tip - bad_tip
    more_cents = int(difference * 100)
    result = more_cents
    return result

print(solution())