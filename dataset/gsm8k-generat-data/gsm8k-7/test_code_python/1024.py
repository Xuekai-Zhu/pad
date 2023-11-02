def solution():
    monday_hours = 10
    tuesday_hours = 8
    remaining_hours = 20
    hourly_rate = 20

    # Calculate the total number of hours worked
    total_hours = monday_hours + tuesday_hours + remaining_hours

    # Calculate the total amount earned for the week
    total_earnings = total_hours * hourly_rate
    result = total_earnings
    return result

print(solution())