def solution():
    """If it takes 3 kangaroos traveling at the same speed a total of 18 hours to travel across a highway, how many hours will it take four turtles, each traveling at half the speed of a kangaroo, to do so?"""
    kangaroos = 3
    kangaroo_speed = 1
    total_distance = kangaroo_speed * 18
    turtle_speed = kangaroo_speed / 2
    turtles = 4
    turtle_time = total_distance / (turtle_speed * turtles)
    result = turtle_time
    return result

print(solution())