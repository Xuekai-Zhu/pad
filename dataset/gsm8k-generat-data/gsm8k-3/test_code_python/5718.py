def solution():
    """Tony made a sandwich with two slices of bread for lunch every day this week. 
    On Saturday, he was extra hungry from doing yard work and made two sandwiches. 
    How many slices of bread are left from the 22-slice loaf Tony started with?"""
    
    # Calculate the total number of slices of bread used for the week
    total_slices_used = 2 * 7 + 2  # 2 slices per day for 7 days plus 2 on Saturday

    # Calculate the remaining number of slices of bread
    slices_left = 22 - total_slices_used

    # Display the number of slices of bread left
    result = slices_left
    return result

print(solution())