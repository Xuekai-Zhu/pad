def solution():
    """Billy ate 20 apples this week. On Monday, he ate 2 apples. On Tuesday, he ate twice as many as he ate the day before. He’s not sure what he ate on Wednesday. On Thursday, he ate four times as many as he ate on Friday. On Friday, he ate half of the amount he ate on Monday. How many apples did he eat on Wednesday?"""
    # Define the number of apples Billy ate on Monday
    apples_monday = 2

    # Define the number of apples Billy ate on Tuesday
    apples_tuesday = apples_monday * 2

    # Define the number of apples Billy ate on Friday
    apples_friday = apples_monday / 2

    # Define the number of apples Billy ate on Thursday
    apples_thursday = apples_friday * 4

    # Calculate the total number of apples Billy ate
    total_apples = apples_monday + apples_tuesday + apples_friday + apples_thursday + x

    # Calculate the number of apples Billy ate on Wednesday (assuming he ate the same amount every day)
    apples_wednesday = (20 - total_apples) / 3

    # Display the number of apples Billy ate on Wednesday
    result = apples_wednesday
    return result

print(solution())