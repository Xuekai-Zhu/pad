def solution():
    """Gina is considered a bad tipper because she tipped 5%. If good tippers tip at least 20%, how many more cents than normal would Gina have to tip on a bill of $26 to be considered a good tipper?"""
    bill = 26
    bad_tip = 0.05 * bill
    good_tip = 0.20 * bill
    difference = good_tip - bad_tip
    more_cents = int(difference * 100)
    result = more_cents
    return result

print(solution())