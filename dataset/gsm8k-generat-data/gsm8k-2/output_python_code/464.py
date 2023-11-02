def solution():
    """A man is returning home from work and trying to decide which route to take. His first route option includes 3 stoplights. This route will take him 10 minutes if all three lights are green, but each light that is red will add 3 minutes to the trip. The second route does not include any stoplights and takes 14 minutes. If the man chooses the first route, how much longer will his trip be if all 3 stoplights are red?"""
    green_time = 10
    red_light_time = 3
    num_lights = 3
    all_red_time = green_time + (num_lights * red_light_time)
    second_route_time = 14
    extra_time = all_red_time - second_route_time
    result = extra_time
    return result

print(solution())