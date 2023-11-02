def solution():
    """On the first day of the journey, the Skipper sailed his ship halfway to the destination by traveling due east for 20 hours at a speed of 30 kilometers per hour, and then turned the ship's engines off to let them cool down. But while the engines were off, a wind storm blew his vessel backward in a westward direction. After the storm, the Skipper used his GPS device to determine the new location of the ship, and he discovered that he was only one-third of the way to his destination. How many kilometers had the ship been blown in a westward direction by the storm?"""
    distance_halfway = 30 * 20
    distance_one_third = distance_halfway * 3
    distance_between_one_third_and_halfway = distance_one_third - distance_halfway
    distance_blown_westward = distance_between_one_third_and_halfway / 2
    result = distance_blown_westward
    return result

print(solution())