def solution():
    # Define the number of hours Monica studied on each day
    wednesday_hours = 2
    thursday_hours = 3 * wednesday_hours
    friday_hours = 0.5 * thursday_hours
    weekend_hours = (wednesday_hours + thursday_hours + friday_hours) * 2

    # Calculate the total number of hours Monica studied during the five days
    total_hours = wednesday_hours + thursday_hours + friday_hours + weekend_hours
    result = total_hours
    return result

print(solution())