def solution():
    release_date = "November 23, 1993"
    weekend_days = ["Saturday", "Sunday"]
    release_day = datetime.datetime.strptime(release_date, "%B %d, %Y").strftime("%A")
    if release_day in weekend_days:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())