def solution():
    rayman_hours = 10  # Rayman works out for 10 hours in a week
    junior_hours = 2 * rayman_hours  # Junior works out for twice the number of hours Rayman works out
    total_hours = rayman_hours + junior_hours  # Combined total number of hours both Rayman and Junior work out
    wolverine_hours = 2 * total_hours  # Wolverine works out for twice the combined total number of hours

    result = wolverine_hours
    return result

print(solution())