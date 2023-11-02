def solution():
    bianca_hours = 12.5  # Bianca worked for 12.5 hours
    celeste_hours = 2 * bianca_hours  # Celeste worked twice as long as Bianca
    mcclain_hours = celeste_hours - 8.5  # McClain worked 8.5 hours less than Celeste

    # Convert all hours to minutes and calculate the total
    total_minutes = (bianca_hours + celeste_hours + mcclain_hours) * 60
    result = total_minutes
    return result

print(solution())