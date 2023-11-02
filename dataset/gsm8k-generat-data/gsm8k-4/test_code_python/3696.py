def solution():
    """Christina walks 7km to school every day from Monday to Friday. She returns home covering the same distance. Last Friday her mother asked her to pass by her friend, which is another 2km away from the school in the opposite distance from home. How many kilometers did Christina cover that week?"""
    # Define the distance Christina walks to and from school each day
    daily_distance = 7 * 2

    # Calculate the distance Christina walks from Monday to Thursday
    monday_to_thursday_distance = daily_distance * 4

    # Calculate the total distance Christina walks including Friday's detour
    total_distance = monday_to_thursday_distance + (daily_distance + 2) + daily_distance

    # Return the total distance
    result = total_distance
    return result

print(solution())