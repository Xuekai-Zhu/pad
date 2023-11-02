def solution():
    watts_per_hour = 125
    hours_per_day = 4
    days_per_week = 7
    cost_per_kwh = 0.14

    # Calculate the total number of watts used per week
    total_watts = watts_per_hour * hours_per_day * days_per_week

    # Convert watts to kilowatts
    total_kwh = total_watts / 1000

    # Calculate the total cost in cents of running the TV for a week
    total_cost = total_kwh * cost_per_kwh * 100
    result = total_cost
    return result

print(solution())