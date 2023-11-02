def solution():
    """Omi is twice as old as Kimiko. Arlette is 3/4 times as old as Kimiko. If Kimiko is 28 years old, calculate the average age of the three."""
    kimiko_age = 28
    omi_age = 2 * kimiko_age
    arlette_age = 0.75 * kimiko_age
    total_age = kimiko_age + omi_age + arlette_age
    average_age = total_age / 3
    result = average_age
    return result

print(solution())