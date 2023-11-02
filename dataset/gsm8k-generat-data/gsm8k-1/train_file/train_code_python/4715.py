def solution():
    """There are 3 bicycles, 4 tricycles and 7 unicycles in the garage at Zoe's house. Each bicycle has 2 wheels, each tricycle has 3 wheels and each unicycle has 1 wheel. How many wheels are there in all?"""
    num_bicycles = 3
    num_tricycles = 4
    num_unicycles = 7

    wheels_per_bicycle = 2
    wheels_per_tricycle = 3
    wheels_per_unicycle = 1

    total_wheels = (num_bicycles * wheels_per_bicycle) + (num_tricycles * wheels_per_tricycle) + (num_unicycles * wheels_per_unicycle)
    result = total_wheels
    return result

print(solution())