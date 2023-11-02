def solution():
    """John skateboarded for 10 miles and then walked another 4 miles to the park. He then skated all the way back home. How many miles has John skateboarded in total?"""
    # Define the distance John walked
    walked_distance = 4

    # Define the total distance John traveled
    total_distance = (walked_distance + 10) * 2

    # Define the distance John skateboarded
    skateboarded_distance = total_distance - walked_distance

    # return the result
    result = skateboarded_distance
    return result

print(solution())