def solution():
    bond_actor = "Sean Connery"
    bond_actor_birthplace = "Scotland"
    washington_monument_location = "Washington, D.C."
    distance_apart = 3500
    if bond_actor_birthplace != washington_monument_location and distance_apart > 500:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())