def solution():
    """Julian has 80 Facebook friends. 60% are boys and 40% are girls. Boyd has twice as many friends who are girls and has 100 friends total. What percentage of Boyd’s friends are boys?"""
    # Define the initial number of Julian's friends and the percentage of boys and girls
    julian_friends = 80
    julian_boys = 0.6
    julian_girls = 0.4

    # Calculate the number of Boyd's girl friends and total friends
    boyd_girls = julian_girls * 2 * julian_friends / 80
    boyd_total_friends = 100

    # Calculate the number and percentage of Boyd's boy friends
    boyd_boys = boyd_total_friends - boyd_girls
    boyd_boys_percentage = (boyd_boys / boyd_total_friends) * 100

    result = boyd_boys_percentage
    return result

print(solution())