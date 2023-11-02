def solution():
    """On a three-day trip, Wendy drove 125 miles on the first day, and 223 miles on the second day. How many miles did she drive on the third day, if the total miles that Wendy drove for the trip is 493 miles?"""
    # Define the distance Wendy drove on the first and second day
    day1_distance = 125
    day2_distance = 223

    # Calculate the distance Wendy drove on the third day
    day3_distance = 493 - day1_distance - day2_distance

    # Display the distance Wendy drove on the third day
    result = day3_distance
    return result

print(solution())