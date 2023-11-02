def solution():
    """Mr. and Mrs. Hugo went on a road trip. On the first day, they traveled 200 miles. 
    On the second day, they traveled 3/4 as far. On the third day, they 
    traveled 1/2 as many miles as the first two days combined. How many miles did they travel for 3 days?"""
    # Define the distance traveled on each day
    day1 = 200
    day2 = day1 * 3/4
    day3 = (day1 + day2) * 1/2

    # Calculate the total distance traveled
    total_distance = day1 + day2 + day3

    # Display the total distance traveled
    result = total_distance
    return result

print(solution())