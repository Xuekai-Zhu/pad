def solution():
    """The tornado picked up the Smith's car and transported it 200 feet in the air before dropping it into the neighbors' pool. Also in the pool was a lawn chair that had been blown twice as far as the car had been transported. And the pool also contained a birdhouse that had flown through the air three times farther than the lawn chair had been blown. How far, in feet, far had the birdhouse flown?"""
    car_distance = 200
    lawn_chair_distance = car_distance * 2
    birdhouse_distance = lawn_chair_distance * 3
    result = birdhouse_distance
    return result

print(solution())