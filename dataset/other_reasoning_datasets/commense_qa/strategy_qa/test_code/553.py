def solution():
    post_office_holidays = ["New Year's Day", "Washington's Birthday", "Veterans Day"]
    unanimously_elected_presidents = ["George Washington"]
    unanimously_elected_birthday_holiday = "Washington's Birthday"
    if unanimously_elected_birthday_holiday in post_office_holidays:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())