def solution():
    """The bald eagle can dive at a speed of 100 miles per hour, while the peregrine falcon can dive at a speed of twice that of the bald eagle. Starting from the same treetop, if it takes the bald eagle 30 seconds to dive to the ground, how long, in seconds, will it take the peregrine falcon to dive the same distance?"""
    # Define the speed of the bald eagle and the peregrine falcon
    eagle_speed = 100  # mph
    falcon_speed = eagle_speed * 2

    # Define the time it takes the bald eagle to dive to the ground
    eagle_time = 30  # seconds

    # Calculate the distance the bald eagle dives using distance = speed * time
    eagle_distance = eagle_speed * (eagle_time / 3600)

    # Calculate the time it will take the peregrine falcon to dive the same distance using time = distance / speed
    falcon_time = eagle_distance / falcon_speed * 3600

    # return the result
    result = falcon_time
    return result

print(solution())