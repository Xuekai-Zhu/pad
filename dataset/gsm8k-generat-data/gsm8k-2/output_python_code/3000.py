def solution():
    """Jamie is in a walking group with 4 other ladies. The ladies all walk 3 miles together. On top of that, Jamie walks an additional 2 miles per day for 6 days while her friend Sue walks half that amount in 6 days. If they walk this same route 6 days a week, how many miles do the ladies walk in total?"""
    group_size = 5
    group_walk_distance = 3
    jamie_additional_distance = 2
    sue_additional_distance = jamie_additional_distance / 2
    additional_days = 6
    total_days = 6
    total_walk_distance = (group_walk_distance * group_size + 
                           (jamie_additional_distance * additional_days * total_days) + 
                           (sue_additional_distance * additional_days * total_days))
    result = total_walk_distance
    return result

print(solution())