def solution():
    """Two birds making a nest each made 10 round trips collecting building materials. If the building materials were located 200 miles from where they were building the nest, what is the total distance the birds covered in the trips?"""
    # Define the number of round trips made by each bird
    num_round_trips = 10

    # Define the distance between the building materials and the nest
    distance = 200

    # Calculate the total distance covered by both birds in their round trips
    total_distance = 2 * 2 * num_round_trips * distance

    # Return the result
    result = total_distance
    return result

print(solution())