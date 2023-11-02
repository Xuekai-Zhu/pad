def solution():
    """There are 3 bicycles, 4 tricycles and 7 unicycles in the garage at Zoe's house. Each bicycle has 2 wheels, each tricycle has 3 wheels and each unicycle has 1 wheel. How many wheels are there in all?"""
    # Define the number of wheels for each type of vehicle
    BICYCLE_WHEELS = 2
    TRICYCLE_WHEELS = 3
    UNICYCLE_WHEELS = 1

    # Define the number of vehicles of each type
    bicycles = 3
    tricycles = 4
    unicycles = 7

    # Calculate the total number of wheels
    total_wheels = (bicycles * BICYCLE_WHEELS) + (tricycles * TRICYCLE_WHEELS) + (unicycles * UNICYCLE_WHEELS)

    # Display the total number of wheels
    result = total_wheels
    return result

print(solution())