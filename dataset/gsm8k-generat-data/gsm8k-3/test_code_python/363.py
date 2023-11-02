def solution():
    """On the first day of the journey, the Skipper sailed his ship halfway to the destination by traveling due east for 20 hours at a speed of 30 kilometers per hour, and then turned the ship's engines off to let them cool down. But while the engines were off, a wind storm blew his vessel backward in a westward direction.
    After the storm, the Skipper used his GPS device to determine the new location of the ship, and he discovered that he was only one-third of the way to his destination.
    How many kilometers had the ship been blown in a westward direction by the storm?"""
    # Calculate the distance the ship traveled due east in the first part of the journey
    distance_east = 30 * 20

    # Calculate the total distance the ship needs to travel to reach the destination
    total_distance = distance_east * 2

    # Calculate the distance the ship traveled after the storm
    distance_west = total_distance / 3

    # Calculate the distance the ship was blown in a westward direction by the storm
    distance_blown = distance_east - distance_west

    # Display the distance the ship was blown in a westward direction by the storm
    result = distance_blown
    return result

print(solution())