def solution():
    """Layla is training for a bicycle race. She rode her bicycle slowly to the high school, rode four miles around the running track at her faster, race pace, and then rode back home, slowly, on the same route. If her total mileage was 10 miles, how far is it, in miles, from Layla's house to the high school?"""
    total_distance = 10
    track_distance = 4
    distance_to_high_school = (total_distance - track_distance) / 2
    result = distance_to_high_school
    return result

print(solution())