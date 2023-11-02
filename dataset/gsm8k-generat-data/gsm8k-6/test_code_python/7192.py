def solution():
    # Calculate Bobby's deadlift at 18 years old
    previous_deadlift = 300
    new_deadlift = 2.5 * previous_deadlift + 100

    # Calculate how much Bobby added per year
    years_passed = 18 - 13
    added_per_year = (new_deadlift - previous_deadlift) / years_passed

    result = added_per_year
    return result

print(solution())