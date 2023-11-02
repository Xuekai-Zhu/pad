def solution():
    total_bill = 140
    shirts_dropped_off = 10
    trousers_dropped_off = 8
    shirts_charged = 5
    trousers_charged = 9
    total_expected = (shirts_dropped_off * shirts_charged) + (trousers_dropped_off * trousers_charged)
    difference = total_bill - total_expected
    shirts_missing = difference / shirts_charged
    result = shirts_missing
    return result

print(solution())