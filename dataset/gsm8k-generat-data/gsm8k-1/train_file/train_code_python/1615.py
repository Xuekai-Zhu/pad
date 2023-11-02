def solution():
    """
    It’s exam season and Tristan has several exams to prepare for. On Monday, he studies for 4 hours then studies for
    twice this long on Tuesday. On Wednesday, Thursday, and Friday he studies for 3 hours each day. He wants to study for
    a total of 25 hours over the week and divides the remaining amount of study time evenly between Saturday and Sunday.
    How many hours does Tristan spend studying on Saturday?
    """
    monday_hours = 4
    tuesday_hours = monday_hours * 2
    wednesday_hours = thursday_hours = friday_hours = 3
    total_hours = 25
    weekday_hours = monday_hours + tuesday_hours + wednesday_hours + thursday_hours + friday_hours
    weekend_hours = (total_hours - weekday_hours) / 2  # divide remaining time evenly between Saturday and Sunday
    saturday_hours = weekend_hours
    result = saturday_hours
    return result

print(solution())