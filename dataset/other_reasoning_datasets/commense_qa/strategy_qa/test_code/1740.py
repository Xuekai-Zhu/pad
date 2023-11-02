def solution():
    original_lead_guitarist = "Dave Mustaine"
    year_fired = 1983
    formed_new_band = True
    megadeth_records_sold = 38_000_000
    if formed_new_band and megadeth_records_sold > 0 and year_fired == 1983:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())