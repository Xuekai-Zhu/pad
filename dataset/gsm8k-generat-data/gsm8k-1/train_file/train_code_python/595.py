def solution():
    """Bianca worked for 12.5 hours last weekend. Celeste worked for twice that amount of time and McClain worked 8.5 hours less than Celeste. How many minutes did the 3 people work in total?"""
    bianca_hours = 12.5
    celeste_hours = bianca_hours * 2
    mcclain_hours = celeste_hours - 8.5
    total_hours = bianca_hours + celeste_hours + mcclain_hours
    total_minutes = total_hours * 60
    result = total_minutes
    return result

print(solution())