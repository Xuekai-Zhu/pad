def solution():
    """For every 100 additional people that board a spaceship, its speed is halved. If the speed of the spaceship with 200 people on board is 500km per hour, what is its speed in km/hr when there are 400 people on board?"""
    current_people = 200
    current_speed = 500
    while current_people < 400:
        current_people += 100
        current_speed /= 2
    result = current_speed
    return result

print(solution())