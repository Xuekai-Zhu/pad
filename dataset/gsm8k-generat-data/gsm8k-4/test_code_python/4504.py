def solution():
    """An old car can drive 8 miles in one hour. After 5 hours of constant driving, the car needs to get cooled down which takes 1 hour. How many miles can this car drive in 13 hours?"""
    # Define the car's speed in miles per hour (mph)
    speed = 8

    # Calculate the distance the car can drive in the first 5 hours
    first_leg_distance = speed * 5

    # Calculate the distance the car can drive in the remaining 7 hours (after cooling down for 1 hour)
    remaining_time = 7
    remaining_distance = speed * remaining_time

    # Calculate the total distance the car can drive in 13 hours
    total_distance = first_leg_distance + remaining_distance

    result = total_distance
    return result

print(solution())