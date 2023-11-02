def solution():
    inches_needed = 54
    inches_now = 48
    inches_to_grow = inches_needed - inches_now
    inches_per_hour = 1/12
    inches_per_month = 1/3

    # Calculate the number of hours per month needed for Alex to grow enough to ride the rollercoaster
    hours_per_month = (inches_to_grow / inches_per_month) - (inches_to_grow / (inches_per_hour * 30))

    result = hours_per_month
    return result

print(solution())