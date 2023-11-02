def solution():
    """Christina walks 7km to school every day from Monday to Friday. She returns home covering the same distance. Last Friday her mother asked her to pass by her friend, which is another 2km away from the school in the opposite distance from home. How many kilometers did Christina cover that week?"""
    # Define the walking distance to school
    DISTANCE_TO_SCHOOL = 7

    # Calculate the total distance walked from Monday to Friday
    distance_walked = DISTANCE_TO_SCHOOL * 2 * 5

    # Add the extra 2km on Friday
    distance_walked += 2

    # Display the total distance walked
    result = distance_walked
    return result

print(solution())