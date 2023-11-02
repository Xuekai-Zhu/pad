def solution():
    """Buoys are placed in the ocean at even intervals away from the beach to help swimmers monitor how far away from the beach they have swum. If a swimmer reaches the third buoy, they have swum out 72 meters. How many meters from the beach is the fourth buoy?"""
    distance_per_buoy = 72 / 3
    distance_to_fourth_buoy = distance_per_buoy * 4
    result = distance_to_fourth_buoy
    return result

print(solution())