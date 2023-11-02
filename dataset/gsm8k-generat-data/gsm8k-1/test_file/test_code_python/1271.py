def solution():
    """John's car breaks down. The car weighs 1200 pounds and he has luggage in it weighing 250 pounds. He also has his two young children who weigh 75 pounds each in it. If the force to move the car is 1% of the weight how much force does he need to push the car?"""
    car_weight = 1200
    luggage_weight = 250
    children_weight = 75 * 2
    total_weight = car_weight + luggage_weight + children_weight
    force_needed = total_weight * 0.01
    result = force_needed
    return result

print(solution())