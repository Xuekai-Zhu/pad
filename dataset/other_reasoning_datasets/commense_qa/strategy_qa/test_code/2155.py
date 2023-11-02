def solution():
    winter_start = "December 20"
    christmas_date = "December 25"
    winter_month = "December"
    if winter_month in christmas_date.lower():
        result = "yes"
    else:
        result = "no"
    return result

print(solution())