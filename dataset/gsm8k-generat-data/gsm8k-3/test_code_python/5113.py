def solution():
    """Two birds making a nest each made 10 round trips collecting building materials. If the building materials were located 200 miles from where they were building the nest, what's the total distance the birds covered in the trips?"""
    
    # Define the distance of each round trip
    round_trip_distance = 2 * 200 # 2 * distance between building materials and nest

    # Calculate the total distance covered by both birds
    total_distance = 2 * round_trip_distance * 10 # 2 birds, 10 round trips each

    # Display the total distance covered
    result = total_distance
    return result

print(solution())