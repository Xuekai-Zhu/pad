def solution():
    """On a three-day trip, Wendy drove 125 miles on the first day, and 223 miles on the second day. How many miles did she drive on the third day, if the total miles that Wendy drove for the trip is 493 miles?"""
    # Define the total miles driven and the miles driven on the first two days
    total_miles = 493
    first_two_days = 125 + 223

    # Calculate the miles driven on the third day by subtracting the miles driven on the first two days from the total miles
    third_day = total_miles - first_two_days

    result = third_day
    return result

print(solution())