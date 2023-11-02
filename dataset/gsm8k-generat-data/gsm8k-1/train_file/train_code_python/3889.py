def solution():
    """Buoys are placed in the ocean at even intervals away from the beach to help swimmers monitor how far away from the beach they have swum. If a swimmer reaches the third buoy, they have swum out 72 meters. How many meters from the beach is the fourth buoy?"""
    third_buoy_distance = 72
    buoy_interval = third_buoy_distance / 3
    fourth_buoy_distance = third_buoy_distance + buoy_interval
    result = fourth_buoy_distance
    return result

print(solution())