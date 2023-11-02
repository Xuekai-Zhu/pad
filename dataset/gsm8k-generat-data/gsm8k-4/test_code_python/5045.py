def solution():
    """Last week, Mr. Sanchez bought 6 feet of rope for their class activity. He found that he lacks rope for the activity so this week, he bought 4 feet less than last week. Since there are 12 inches in a foot, how many inches of ribbon did Mr. Sanchez buy in all?"""
    # Define the length of rope bought last week
    last_week = 6

    # Calculate the length of rope bought this week
    this_week = last_week - 4

    # Calculate the total length of rope bought in feet
    total_feet = last_week + this_week

    # Convert the length in feet to inches
    total_inches = total_feet * 12

    # return the result
    result = total_inches
    return result

print(solution())