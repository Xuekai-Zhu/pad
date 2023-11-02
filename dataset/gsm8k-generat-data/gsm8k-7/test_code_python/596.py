def solution():
    bianca_hours = 12.5
    celeste_hours = bianca_hours * 2
    mcclain_hours = celeste_hours - 8.5

    # Calculate the total hours worked by all three people
    total_hours = bianca_hours + celeste_hours + mcclain_hours

    # Convert hours to minutes
    total_minutes = total_hours * 60
    result = total_minutes
    return result

print(solution())