def solution():
    conflict_start_date = "hundreds of years ago"
    england_occupation_end_date = "1945"
    england_arab_alliance_date = "during Israel's war for independence"
    if england_occupation_end_date <= england_arab_alliance_date:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())