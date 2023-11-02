def solution():
    people_per_family = 4
    total_capacity = 300 * people_per_family
    voyage_started_at = total_capacity - (100 * people_per_family)
    result = voyage_started_at
    return result

print(solution())