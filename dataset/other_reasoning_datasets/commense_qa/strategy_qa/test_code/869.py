def solution():
    asteroid_size = 583 #in miles
    can_create_gravity = asteroid_size > 400 #in miles
    if can_create_gravity:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())