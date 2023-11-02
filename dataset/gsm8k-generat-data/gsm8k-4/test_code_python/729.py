def solution():
    """John jogs at a speed of 4 miles per hour when he runs alone, but runs at 6 miles per hour when he is being dragged by his 100-pound German Shepherd dog. If John and his dog go on a run together for 30 minutes, and then John runs for an additional 30 minutes by himself, how far will John have traveled?"""
    
    # Calculate the distance traveled by John and his dog during the first 30 minutes 
    distance_together = (4 + 6) / 2 * (30 / 60)
    
    # Calculate the distance traveled by John for the additional 30 minutes 
    distance_alone = 4 * (30 / 60)
    
    # Calculate the total distance traveled by John in an hour 
    total_distance = distance_together + distance_alone
    
    # Return the total distance traveled by John in miles 
    result = total_distance
    return result

print(solution())