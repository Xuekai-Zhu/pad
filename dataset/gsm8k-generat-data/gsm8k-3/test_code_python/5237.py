def solution():
    """Wanda walks her daughter .5 miles to school in the morning and then walks .5 miles home. She repeats this when she meets her daughter after school in the afternoon. They walk to school 5 days a week. How many miles does Wanda walk after 4 weeks?"""
    # Define the distance Wanda walks per trip
    distance_per_trip = 0.5 + 0.5

    # Calculate the total distance Wanda walks in a week
    distance_per_week = distance_per_trip * 2 * 5

    # Calculate the total distance Wanda walks in 4 weeks
    total_distance = distance_per_week * 4

    # Display the total distance
    result = total_distance
    return result

print(solution())