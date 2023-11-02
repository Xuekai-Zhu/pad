def solution():
    total_hours_required = 1500
    hours_completed = 50 + 9 + 121
    hours_per_month = 220

    # Calculate the remaining hours that Rita needs to complete
    remaining_hours = total_hours_required - hours_completed

    # Calculate the number of months that Rita needs to fulfill her coach's requirements
    num_months = remaining_hours / hours_per_month
    result = num_months
    return result

print(solution())