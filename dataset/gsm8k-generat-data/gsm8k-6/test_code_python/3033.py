def solution():
    # Calculate the distance traveled by the car, lawn chair, and birdhouse
    car_distance = 200  # the car was transported 200 feet in the air
    lawn_chair_distance = 2 * car_distance  # the lawn chair was blown twice as far as the car
    birdhouse_distance = 3 * lawn_chair_distance  # the birdhouse flew three times farther than the lawn chair

    result = birdhouse_distance
    return result

print(solution())