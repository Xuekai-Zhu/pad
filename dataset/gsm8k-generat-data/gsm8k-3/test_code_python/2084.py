def solution():
    """Timmy's parents have a 2 car garage, which has both cars inside it.  Also inside is a riding lawnmower, a bicycle for Timmy as well as each of his parents, a tricycle for Timmy's little brother Joey, and a unicycle that Timmy's dad practices riding on.  How many wheels in total are in this garage?"""
    # Define the number of wheels on each type of vehicle
    CAR_WHEELS = 4
    LAWNMOWER_WHEELS = 4
    BICYCLE_WHEELS = 2
    TRICYCLE_WHEELS = 3
    UNICYCLE_WHEELS = 1

    # Calculate the total number of wheels in the garage
    total_wheels = 2 * CAR_WHEELS + LAWNMOWER_WHEELS + 3 * BICYCLE_WHEELS + TRICYCLE_WHEELS + UNICYCLE_WHEELS

    # Display the total number of wheels
    result = total_wheels
    return result

print(solution())