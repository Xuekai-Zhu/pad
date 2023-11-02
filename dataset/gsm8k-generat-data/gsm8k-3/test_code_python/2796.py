def solution():
    """Julian has 80 Facebook friends. 60% are boys and 40% are girls. Boyd has twice as many friends who are girls and has 100 friends total. What percentage of Boyd’s friends are boys?"""
    # Define the number of Julian's boy and girl friends
    julian_total_friends = 80
    julian_boy_friends = julian_total_friends * 0.6
    julian_girl_friends = julian_total_friends * 0.4

    # Calculate the number of Boyd's girl friends
    boyd_girl_friends = (100 / 3) * 2

    # Calculate the number of Boyd's boy friends
    boyd_boy_friends = 100 - boyd_girl_friends

    # Calculate the percentage of Boyd's friends who are boys
    boy_percentage = (boyd_boy_friends / 100) * 100

    # Display the percentage of Boyd's friends who are boys
    result = boy_percentage
    return result

print(solution())