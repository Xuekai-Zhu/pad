def solution():
    """It takes 5 people to lift a car and twice as many people to lift a truck. How many people are needed to lift 6 cars and 3 trucks?"""
    car_people = 5
    truck_people = 2 * car_people
    total_people = 6 * car_people + 3 * truck_people
    result = total_people
    return result

print(solution())