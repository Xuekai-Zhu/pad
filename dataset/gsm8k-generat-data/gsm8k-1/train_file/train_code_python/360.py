def solution():
    """On the first day of the journey, the Skipper sailed his ship halfway to the destination by traveling due east for 20 hours at a speed of 30 kilometers per hour, and then turned the ship's engines off to let them cool down. But while the engines were off, a wind storm blew his vessel backward in a westward direction.  After the storm, the Skipper used his GPS device to determine the new location of the ship, and he discovered that he was only one-third of the way to his destination.  How many kilometers had the ship been blown in a westward direction by the storm?"""
    distance_to_destination = 2/3
    time_sailed_due_east = 20
    speed_sailed_due_east = 30
    distance_sailed_due_east = time_sailed_due_east * speed_sailed_due_east
    distance_blown_westward = distance_sailed_due_east - distance_to_destination * distance_sailed_due_east
    result = distance_blown_westward
    return result

print(solution())