def solution():
    previous_deadlift = 300  # Bobby's previous deadlift at 13 was 300 pounds
    current_deadlift = (250/100)*previous_deadlift + 100  # Bobby's current deadlift at 18
    years_passed = 18 - 13  # Bobby's age difference between the two deadlifts

    # Calculate the amount Bobby added per year to his deadlift
    added_per_year = (current_deadlift - previous_deadlift) / years_passed
    result = added_per_year
    return result

print(solution())