def solution():
    # Define the initial amount of sugar and the amount removed in one hour
    initial_sugar = 24
    sugar_per_hour = 4

    # Calculate the amount of sugar remaining after three hours
    remaining_sugar = initial_sugar - (sugar_per_hour * 3)

    # Calculate the number of hours needed to harvest the remaining sugar
    remaining_hours = remaining_sugar / sugar_per_hour
    result = remaining_hours
    return result

print(solution())