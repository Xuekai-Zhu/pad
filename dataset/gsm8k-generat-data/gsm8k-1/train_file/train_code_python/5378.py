def solution():
    """Gina is considered a bad tipper because she tipped 5%. If good tippers tip at least 20%, how many more cents than normal would Gina have to tip on a bill of $26 to be considered a good tipper?"""
    bill = 26
    bad_tip_percent = 5
    good_tip_percent = 20
    bad_tip_amount = bill * (bad_tip_percent / 100)
    good_tip_amount = bill * (good_tip_percent / 100)
    difference = good_tip_amount - bad_tip_amount
    more_cents = difference * 100
    result = more_cents
    return result

print(solution())