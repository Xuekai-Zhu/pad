def solution():
    total_hours = 5  # Janet goes to the gym for a total of 5 hours per week
    monday_wednesday_hours = 1.5 * 2  # Janet spends 1.5 hours at the gym on both Monday and Wednesday
    remaining_hours = total_hours - monday_wednesday_hours  # Calculate the number of remaining hours for Tuesday and Friday
    friday_hours = remaining_hours / 2  # Divide the remaining hours equally between Tuesday and Friday

    result = friday_hours
    return result

print(solution())