def solution():
    weekdays_rate = 420
    weekend_rate = 540
    days_rented = 4
    day1 = "Thursday"
    day2 = "Friday"
    day3 = "Saturday"
    day4 = "Sunday"
    if day1 == "Thursday" or day2 == "Friday":
        weekdays_rented = 2
        cost_per_person = (weekdays_rate * weekdays_rented + weekend_rate * (days_rented - weekdays_rented)) / 5
        return cost_per_person
    else:
        weekend_rented = 2
        cost_per_person = (weekend_rate * weekend_rented + weekdays_rate * (days_rented - weekend_rented)) / 5
        return cost_per_person

print(solution())