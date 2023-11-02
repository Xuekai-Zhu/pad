def solution():
    
    monday_hours = 2
    wednesday_hours = 1
    friday_hours = 3
    total_hours = monday_hours + wednesday_hours + friday_hours
    weekly_earnings = total_hours * 5
    bike_cost = 180
    weeks_to_work = bike_cost / weekly_earnings
    result = weeks_to_work
    return result

print(solution())