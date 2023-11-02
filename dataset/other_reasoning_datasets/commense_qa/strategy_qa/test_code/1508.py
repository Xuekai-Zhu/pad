def solution():
    winter_start_month = "December"
    winter_end_month = "March"
    government_holidays = {
        "Christmas": "December 25",
        "New Year": "January 1",
        "King Day": "a Monday in the middle of January",
        "President's Day": "a Monday in late February"
    }
    winter_holidays = []
    for holiday in government_holidays:
        holiday_month = government_holidays[holiday].split()[0]
        if winter_start_month <= holiday_month <= winter_end_month:
            winter_holidays.append(holiday)
    if len(winter_holidays) > 1:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())