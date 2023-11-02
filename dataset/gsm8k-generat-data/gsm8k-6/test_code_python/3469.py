def solution():
    rayman_hours = 10   # Rayman works out for 10 hours in a week
    junior_hours = rayman_hours * 2   # Junior works out for twice the hours of Rayman
    total_hours = rayman_hours + junior_hours   # Total hours both Rayman and Junior workout
    wolverine_hours = total_hours * 2   # Wolverine works out for twice the total hours of both Rayman and Junior
    result = wolverine_hours
    return result

print(solution())