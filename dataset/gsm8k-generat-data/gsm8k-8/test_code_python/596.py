def solution():
    # Calculate Bianca's total minutes worked
    bianca_minutes = 12.5 * 60

    # Calculate Celeste's total minutes worked
    celeste_minutes = 2 * bianca_minutes

    # Calculate McClain's total minutes worked
    mcclain_minutes = celeste_minutes - (8.5 * 60)

    # Calculate the total minutes worked by all three people
    total_minutes = bianca_minutes + celeste_minutes + mcclain_minutes
    result = total_minutes
    return result

print(solution())