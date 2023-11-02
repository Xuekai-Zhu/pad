def solution():
    """On the first day of the journey, the Skipper sailed his ship halfway to the destination by traveling due east for 20 hours at a speed of 30 kilometers per hour, and then turned the ship's engines off to let them cool down. But while the engines were off, a wind storm blew his vessel backward in a westward direction. After the storm, the Skipper used his GPS device to determine the new location of the ship, and he discovered that he was only one-third of the way to his destination. How many kilometers had the ship been blown in a westward direction?"""
    # Define the variables
    distance_to_destination = None
    westward_distance = None
    time = 20
    speed = 30

   
    distance_traveled = time * speed

    # Calculate the distance to the destination
    distance_to_destination = distance_traveled * 2

    # Calculate the distance traveled after being blown back by the storm
    distance_after_storm = distance_to_destination / 3

    # Calculate the westward distance
    westward_distance = distance_to_destination - distance_after_storm

    # return the result
    result = westward_distance
    return result

print(solution())