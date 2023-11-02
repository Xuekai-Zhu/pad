def solution():
    """A baseball cap factory made 320 caps the first week, 400 the second week, and 300 the third week.  If the company makes their average number of caps from the first 3 weeks during the fourth week, how many total caps will they make?"""
    # Define the number of caps made in each of the first 3 weeks
    week1_caps = 320
    week2_caps = 400
    week3_caps = 300

    # Calculate the average number of caps made in the first 3 weeks
    avg_caps = (week1_caps + week2_caps + week3_caps) / 3

    # Calculate the total number of caps made in the fourth week
    week4_caps = avg_caps

    # Calculate the total number of caps made over the 4 weeks
    total_caps = week1_caps + week2_caps + week3_caps + week4_caps

    # Display the total number of caps made
    result = total_caps
    return result

print(solution())