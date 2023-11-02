def solution():
    """The bald eagle can dive at a speed of 100 miles per hour, while the peregrine falcon can dive at a speed of twice that of the bald eagle. Starting from the same treetop, if it takes the bald eagle 30 seconds to dive to the ground, how long, in seconds, will it take the peregrine falcon to dive the same distance?"""
    bald_eagle_speed = 100
    peregrine_falcon_speed = 2 * bald_eagle_speed
    bald_eagle_time = 30
    distance = bald_eagle_speed * (bald_eagle_time / 60 / 60)
    peregrine_falcon_time = distance / peregrine_falcon_speed * 60 * 60
    result = peregrine_falcon_time
    return result

print(solution())