def solution():
    num_monday = 10
    num_tuesday = 15
    num_wednesday = 10
    num_thursday = 10
    num_friday = 10

    # Calculate the total number of people who attended class during the week
    total_people = num_monday + num_tuesday + num_wednesday + num_thursday + num_friday

    # Calculate the average number of people who attended class each day
    avg_people_per_day = total_people / 5
    result = avg_people_per_day
    return result

print(solution())