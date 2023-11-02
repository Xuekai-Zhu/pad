def solution():
    """Layla is training for a bicycle race. She rode her bicycle slowly to the high school, rode four miles around the running track at her faster, race pace, and then rode back home, slowly, on the same route. If her total mileage was 10 miles, how far is it, in miles, from Layla's house to the high school?"""
    total_mileage = 10
    race_mileage = 4
    slow_mileage = (total_mileage - race_mileage) / 2
    distance_to_highschool = slow_mileage
    result = distance_to_highschool
    return result

print(solution())