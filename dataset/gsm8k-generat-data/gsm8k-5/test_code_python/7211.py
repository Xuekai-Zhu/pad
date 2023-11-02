def solution():
    ivy_stripped_per_day = 6  # Cary strips 6 feet of ivy every day
    ivy_grown_per_night = 2  # The ivy grows 2 feet every night
    total_ivy = 40  # The tree is covered by 40 feet of ivy

    # Calculate the number of days it will take Cary to strip all the ivy
    days = 0
    while total_ivy > 0:
        days += 1
        total_ivy -= ivy_stripped_per_day
        if total_ivy <= 0:
            break
        total_ivy += ivy_grown_per_night

    result = days
    return result

print(solution())