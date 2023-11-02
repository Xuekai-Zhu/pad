def solution():
    """There are 100 people in a theater. If 19 of these people have blue eyes, half of them have brown eyes, a quarter have black eyes, and the rest have green eyes, how many of them have green eyes?"""
    total_people = 100
    blue_eyes = 19
    brown_eyes = total_people / 2
    black_eyes = total_people / 4
    green_eyes = total_people - blue_eyes - brown_eyes - black_eyes
    result = green_eyes
    return result

print(solution())