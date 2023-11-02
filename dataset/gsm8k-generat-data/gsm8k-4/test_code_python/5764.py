def solution():
    """Two old ladies spent the afternoon walking through Central Park. The first lady walked twice as far as the second lady. If the second lady walked four miles, what is the combined total distance, in miles, the two ladies walked?"""
    # Define the distance walked by the second lady
    second_lady_distance = 4

    # Calculate the distance walked by the first lady
    first_lady_distance = 2 * second_lady_distance

    # Calculate the combined distance walked by both ladies
    total_distance = first_lady_distance + second_lady_distance

    # Return the result
    result = total_distance
    return result

print(solution())