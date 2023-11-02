def solution():
    """A captain steers his ship 100 miles north on the first day of their journey. On the second day, he sails to the east three times as far as the distance as he covered on the first day. On the third day, the ship travels further east for 110 more miles than the distance it covered on the second day. What is the total distance the ship has traveled in the three days?"""
    # Define the distance sailed on the first day
    day1_distance = 100

    # Define the distance sailed on the second day
    day2_distance = day1_distance * 3

    # Define the distance sailed on the third day
    day3_distance = day2_distance + 110

    # Calculate the total distance traveled
    total_distance = day1_distance + day2_distance + day3_distance

    # Return the result
    result = total_distance
    return result

print(solution())