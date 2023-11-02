def solution():
    distance = 6  # miles
    monday_speed = 2  # miles per hour
    wednesday_speed = 3  # miles per hour
    friday_speed = 6  # miles per hour

    # Calculate the time it takes on Monday to walk the 6 miles
    monday_time = distance / monday_speed

    # Calculate the time it takes on Wednesday to walk the 6 miles
    wednesday_time = distance / wednesday_speed

    # Calculate the time it takes on Friday to run the 6 miles
    friday_time = distance / friday_speed

    # Calculate the total time spent exercising in a week
    total_time = monday_time + wednesday_time + friday_time
    result = total_time
    return result

print(solution())