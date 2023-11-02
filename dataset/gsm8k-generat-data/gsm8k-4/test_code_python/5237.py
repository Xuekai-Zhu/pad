def solution():
    """Wanda walks her daughter .5 miles to school in the morning and then walks .5 miles home. She repeats this when she meets her daughter after school in the afternoon. They walk to school 5 days a week. How many miles does Wanda walk after 4 weeks?"""
    # Define the distance walked by Wanda and her daughter in one round trip to school
    round_trip_distance = 1

    # Define the number of days Wanda walks her daughter to school in a week
    days_per_week = 5

    # Calculate the distance Wanda walks in a week
    weekly_distance = round_trip_distance * 2 * days_per_week

    # Calculate the distance Wanda walks in 4 weeks
    monthly_distance = weekly_distance * 4

    result = monthly_distance
    return result

print(solution())