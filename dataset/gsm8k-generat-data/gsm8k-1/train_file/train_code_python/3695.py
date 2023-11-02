def solution():
    """Christina walks 7km to school every day from Monday to Friday. She returns home covering the same distance. Last Friday her mother asked her to pass by her friend, which is another 2km away from the school in the opposite distance from home. How many kilometers did Christina cover that week?"""
    distance_to_school = 7
    days_without_friday = 4
    distance_from_school_to_friend = 2
    total_distance_without_friday = distance_to_school * days_without_friday * 2  # round-trip
    total_distance_on_friday = distance_to_school * 2 + distance_from_school_to_friend * 2 # round-trip
    total_distance = total_distance_without_friday + total_distance_on_friday
    result = total_distance
    return result

print(solution())