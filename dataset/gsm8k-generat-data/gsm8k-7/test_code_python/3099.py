def solution():
    natasha_minutes = 30 * 7
    esteban_minutes = 10 * 9

    # Convert minutes to hours
    natasha_hours = natasha_minutes / 60
    esteban_hours = esteban_minutes / 60

    total_hours = natasha_hours + esteban_hours
    result = total_hours
    return result

print(solution())