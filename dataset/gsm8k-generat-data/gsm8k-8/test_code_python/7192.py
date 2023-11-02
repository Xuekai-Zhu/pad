def solution():
    # Calculate Bobby's previous deadlift at age 18
    previous_deadlift = 300

    # Calculate Bobby's current deadlift at age 18
    current_deadlift = 250/100 * previous_deadlift + 100

    # Calculate the increase in deadlift over 5 years
    increase = current_deadlift - previous_deadlift

    # Calculate the average increase per year
    average_increase = increase / 5
    result = average_increase
    return result

print(solution())