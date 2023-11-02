def solution():
    # Calculate the total number of hours Jake spent watching the show before Friday
    monday_hours = 12
    tuesday_hours = 4
    wednesday_hours = 12/4
    total_hours = monday_hours + tuesday_hours + wednesday_hours

    # Calculate the number of hours Jake spent on Thursday
    thursday_hours = total_hours/2

    # Calculate the number of hours Jake spent watching the show on Friday
    friday_hours = 52 - total_hours - thursday_hours

    result = friday_hours
    return result

print(solution())