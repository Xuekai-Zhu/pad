def solution():
    """Christina walks 7km to school every day from Monday to Friday. She returns home covering the same distance. Last Friday her mother asked her to pass by her friend, which is another 2km away from the school in the opposite distance from home. How many kilometers did Christina cover that week?"""
    daily_distance = 7 * 2 # round trip
    extra_distance = 2
    total_distance = daily_distance * 5 + extra_distance
    result = total_distance
    return result

print(solution())