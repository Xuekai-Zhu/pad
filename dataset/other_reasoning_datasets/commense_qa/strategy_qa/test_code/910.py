def solution():
    curing_time = 2 # months
    slaughtering_month = "December"
    new_years_month = "January"
    if new_years_month not in [slaughtered_month, slaughtered_month + 1]: # Parma ham won't be ready for New Year's
        result = "no"
    else:
        if slaughtering_month == "November":
            months_until_new_years = 1
        else:
            months_until_new_years = 12 - (ord(slaughtering_month) - 96) + 1 # Convert month name to number
        if months_until_new_years >= curing_time:
            result = "yes"
        else:
            result = "no"
    return result

print(solution())