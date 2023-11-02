def solution():
    """Layla is training for a bicycle race. She rode her bicycle slowly to the high school, rode four miles around the running track at her faster, race pace, and then rode back home, slowly, on the same route. If her total mileage was 10 miles, how far is it, in miles, from Layla's house to the high school?"""
    # Let x be the distance from Layla's house to the high school
    # Layla rides x miles to the high school, then 4 miles on the track, and x miles back home
    # The total distance is 2x + 4 = 10
    # Solve for x
    x = (10 - 4) / 2

    # Display the distance from Layla's house to the high school
    result = x
    return result

print(solution())