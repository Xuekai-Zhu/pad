def solution():
    reps = 50  # The retail store wants to hire 50 phone reps
    hours_per_day = 8  # Each phone rep will work 8 hours a day
    wage_per_hour = 14  # Each phone rep will be paid $14.00 an hour
    days = 5  # The reps will work for 5 days

    # Calculate the total amount of money the company will pay all 50 new employees after 5 days
    total_pay = reps * hours_per_day * wage_per_hour * days

    result = total_pay
    return result

print(solution())