def solution():
    """Buoys are placed in the ocean at even intervals away from the beach to help swimmers monitor how far away from the beach they have swum. If a swimmer reaches the third buoy, they have swum out 72 meters. How many meters from the beach is the fourth buoy?"""
    # Define the distance between each buoy
    DISTANCE_BETWEEN_BUOYS = 24

    # Calculate the distance from the beach to the third buoy
    distance_to_third_buoy = 72

    # Calculate the distance from the beach to the fourth buoy
    distance_to_fourth_buoy = distance_to_third_buoy + DISTANCE_BETWEEN_BUOYS

    # Display the distance from the beach to the fourth buoy
    result = distance_to_fourth_buoy
    return result

print(solution())