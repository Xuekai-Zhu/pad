def solution():
    """Jamie is in a walking group with 4 other ladies.  The ladies all walk 3 miles together.  On top of that, Jamie walks an additional 2 miles per day for 6 days while her friend Sue walks half that amount in 6 days.  If they walk this same route 6 days a week, how many miles do the ladies walk in total?"""
    
    # Calculate the total distance Jamie walks in addition to the group walk
    jamie_extra_distance = 2 * 6
    
    # Calculate the total distance Sue walks in addition to the group walk
    sue_extra_distance = 1 * 6
    
    # Calculate the total distance walked by the group, Jamie, and Sue
    total_distance = (3 + jamie_extra_distance + sue_extra_distance) * 6 * 5
    
    # Display the total distance walked
    result = total_distance
    return result

print(solution())