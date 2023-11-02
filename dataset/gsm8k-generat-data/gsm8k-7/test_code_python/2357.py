def solution():
    clown_cost_per_hour = 100
    clown_hours = 4

    bounce_house_cost_per_hour = clown_cost_per_hour * 3
    bounce_house_hours = clown_hours / 2

    other_party_cost = 1000

    total_cost = (clown_cost_per_hour * clown_hours) + (bounce_house_cost_per_hour * bounce_house_hours) + other_party_cost
    result = total_cost
    return result

print(solution())