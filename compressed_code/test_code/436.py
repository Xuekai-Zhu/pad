def solution():
    
    bianca_hours = 12.5
    celeste_hours = 2 * bianca_hours
    mcclain_hours = celeste_hours - 8.5
    total_hours = bianca_hours + celeste_hours + mcclain_hours
    total_minutes = total_hours * 60
    result = total_minutes
    return result

print(solution())