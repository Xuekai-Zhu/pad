def solution():
    regular_rate = 20  # Jamie earns $20 per hour for 8 hours of work
    additional_hours = 8  # Jamie needs to work additional hours
    special_rate = regular_rate * 0.7  # Jamie is paid a special hourly rate that is 150% of her regular rate
    last_tuesday_hours = 11  # Jamie worked 11 hours of work

    # Calculate Jamie's regular hourly rate
    regular_rate = regular_rate * regular_hours

    # Calculate Jamie's special hourly rate
    special_rate = special_rate * additional_hours

    # Calculate Jamie's total pay for Jamie's work that day
    total_pay = regular_rate + special_rate
    result = total_pay
    return result

print(solution())