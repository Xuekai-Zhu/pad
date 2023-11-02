def solution():
    # Define the total number of homework hours in a week
    total_homework_hours = 2 * 5 + 5

    # Subtract the hours Paul spends at practice
    available_homework_hours = total_homework_hours - 2 * 2

    # Divide by the number of remaining weeknights
    remaining_weeknights = 5 - 2
    average_homework_hours = available_homework_hours / remaining_weeknights
    result = average_homework_hours
    return result

print(solution())