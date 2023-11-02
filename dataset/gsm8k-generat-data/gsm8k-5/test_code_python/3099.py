def solution():
    # Calculate the total time Natasha exercised in minutes
    natasha_minutes = 30 * 7

    # Calculate the total time Esteban exercised in minutes
    esteban_minutes = 10 * 9

    # Convert both totals to hours
    natasha_hours = natasha_minutes / 60
    esteban_hours = esteban_minutes / 60

    # Calculate the total time both of them exercised in hours
    total_hours = natasha_hours + esteban_hours
    result = total_hours
    return result

print(solution())