def solution():
    """There are 3 bicycles, 4 tricycles and 7 unicycles in the garage at Zoe's house. Each bicycle has 2 wheels, each tricycle has 3 wheels and each unicycle has 1 wheel. How many wheels are there in all?"""
    # Define the number of each type of vehicle and the number of wheels per vehicle
    bicycles = 3
    tricycles = 4
    unicycles = 7
    bike_wheels = 2
    trike_wheels = 3
    uni_wheels = 1

    # Calculate the total number of wheels
    total_wheels = bicycles * bike_wheels + tricycles * trike_wheels + unicycles * uni_wheels

    # return the result
    result = total_wheels
    return result

print(solution())