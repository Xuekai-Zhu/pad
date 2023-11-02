def solution():
    """Mary has 26 blue shirts and 36 brown shirts. If she gives away half of her blue shirts and a third of her brown shirts, how many shirts does she have left?"""
    # Define the initial number of blue and brown shirts
    blue_shirts = 26
    brown_shirts = 36

    # Calculate the number of blue shirts Mary gives away
    blue_giveaway = blue_shirts / 2

    # Calculate the number of brown shirts Mary gives away
    brown_giveaway = brown_shirts / 3

    # Calculate the number of shirts Mary has left
    blue_left = blue_shirts - blue_giveaway
    brown_left = brown_shirts - brown_giveaway
    total_left = blue_left + brown_left

    # return the result
    result = total_left
    return result

print(solution())