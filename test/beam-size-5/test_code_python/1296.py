def solution():
    cars_per_day = 3  # Josh services 3 cars per day
    days_per_week = 7  # There are 7 days in a week
    weeks = 2  # Josh wants to know how much he makes in 2 weeks

    # Calculate the total number of cars Josh makes in 2 weeks
    total_cars = cars_per_day * days_per_week * weeks

    # Calculate the total amount of money Josh makes in 2 weeks
    total_money = total_cars * 4
    result = total_money
    return result

print(solution())