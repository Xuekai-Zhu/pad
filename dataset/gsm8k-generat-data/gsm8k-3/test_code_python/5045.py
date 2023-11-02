def solution():
    """Last week, Mr. Sanchez bought 6 feet of rope for their class activity. He found that he lacks rope for the activity so this week, he bought 4 feet less than last week. Since there are 12 inches in a foot, how many inches of ribbon did Mr. Sanchez buy in all?"""
    # Define the length of rope in feet
    rope_last_week = 6
    rope_this_week = rope_last_week - 4

    # Define the conversion factor for feet to inches
    feet_to_inches = 12

    # Calculate the total length of rope in inches
    total_rope_inches = (rope_last_week + rope_this_week) * feet_to_inches

    # Display the total length of rope in inches
    result = total_rope_inches
    return result

print(solution())