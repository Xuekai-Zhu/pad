def solution():
    """There are 3 bicycles, 4 tricycles and 7 unicycles in the garage at Zoe's house. Each bicycle has 2 wheels, each tricycle has 3 wheels and each unicycle has 1 wheel. How many wheels are there in all?"""
    bicycle_wheels = 3 * 2
    tricycle_wheels = 4 * 3
    unicycle_wheels = 7 * 1
    total_wheels = bicycle_wheels + tricycle_wheels + unicycle_wheels
    result = total_wheels
    return result

print(solution())