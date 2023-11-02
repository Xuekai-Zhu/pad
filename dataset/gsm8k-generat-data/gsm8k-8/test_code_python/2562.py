def solution():
    # Calculate the number of potatoes Jason can eat in 1 minute
    potatoes_per_minute = 3/20

    # Calculate the total number of minutes it would take for Jason to eat 27 potatoes
    total_minutes = 27/potatoes_per_minute

    # Convert minutes to hours
    total_hours = total_minutes/60
    result = total_hours
    return result

print(solution())