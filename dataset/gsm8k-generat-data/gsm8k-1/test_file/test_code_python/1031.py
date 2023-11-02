def solution():
    """Richard wants to make a video to share online of him doing a science experiment that creates a fountain of diet soda after placing a specific branded candy inside it. Richard's driveway is 24 feet wide and he wants to put a bottle of soda every 3 feet of the driveway. After starting at the first bottle, it will take Richard 5 seconds to go from one soda bottle to the next, dropping the candy in. How many seconds total will it take Richard to set off all the soda fountains?"""
    driveway_width = 24
    distance_between_bottles = 3
    number_of_bottles = int(driveway_width / distance_between_bottles)
    time_per_bottle = 5
    total_time = number_of_bottles * time_per_bottle
    result = total_time
    return result

print(solution())