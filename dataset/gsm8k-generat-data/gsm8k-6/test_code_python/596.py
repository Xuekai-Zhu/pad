def solution():
    # Calculate the number of hours each person worked
    bianca_hours = 12.5
    celeste_hours = 2 * bianca_hours
    mcclain_hours = celeste_hours - 8.5

    # Calculate the total hours worked
    total_hours = bianca_hours + celeste_hours + mcclain_hours

    # Convert total hours to minutes
    total_minutes = total_hours * 60

    result = total_minutes
    return result

print(solution())