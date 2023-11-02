def solution():
    total_hours_worked = 23 + 8
    total_earnings = 460
    cost_of_console = 600
    cost_of_car_fix = 340

    # Calculate Sam's hourly rate
    hourly_rate = total_earnings / total_hours_worked

    # Calculate how much Sam has saved after fixing his car
    total_savings = total_earnings - cost_of_car_fix

    # Calculate how much more Sam needs to save for the console
    remaining_savings_needed = cost_of_console - total_savings

    # Calculate how many more hours Sam needs to work to earn the remaining savings needed
    additional_hours_needed = remaining_savings_needed / hourly_rate
    result = additional_hours_needed
    return result

print(solution())