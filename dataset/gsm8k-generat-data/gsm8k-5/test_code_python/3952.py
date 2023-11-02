def solution():
    # Calculate the speed Luis is driving in miles per minute
    speed = 80 / 120  # 80 miles in 2 hours = 80/2 = 40 miles in 1 hour, 40/60= 2/3 miles per minute

    # Calculate the distance Luis will go in 15 minutes
    distance = speed * 15  # speed is in miles per minute and 15 minutes is the time

    result = distance
    return result

print(solution())