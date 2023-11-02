def solution():
    """In a week, Rayman works out for half the number of hours Junior takes to work out. Wolverine, their friend, works out for twice the combined total number of hours both Rayman and Junior take during their workouts. Calculate the number of hours Wolverine takes doing her workouts if Rayman does workouts for 10 hours in a week."""
    rayman_hours = 10
    junior_hours = rayman_hours * 2
    wolverine_hours = 2 * (rayman_hours + junior_hours)
    result = wolverine_hours
    return result

print(solution())