def solution():
    """Henry made two stops during his 60-mile bike trip. He first stopped after 20 miles. His second stop was 15 miles before the end of the trip. How many miles did he travel between his first and second stops?"""
    total_distance = 60
    first_stop_distance = 20
    second_stop_distance = total_distance - 15
    distance_between_stops = second_stop_distance - first_stop_distance
    result = distance_between_stops
    return result

print(solution())