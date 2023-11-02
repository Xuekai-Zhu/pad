def solution():
    """In today's field day challenge, the 4th graders were competing against the 5th graders.  Each grade had 2 different classes.  The first 4th grade class had 12 girls and 13 boys.  The second 4th grade class had 15 girls and 11 boys.  The first 5th grade class had 9 girls and 13 boys while the second 5th grade class had 10 girls and 11 boys.  In total, how many more boys were competing than girls?"""
    # Calculate the total number of girls in 4th grade
    total_4th_girls = 12 + 15

    # Calculate the total number of boys in 4th grade
    total_4th_boys = 13 + 11

    # Calculate the total number of girls in 5th grade
    total_5th_girls = 9 + 10

    # Calculate the total number of boys in 5th grade
    total_5th_boys = 13 + 11

    # Calculate the total number of girls
    total_girls = total_4th_girls + total_5th_girls

    # Calculate the total number of boys
    total_boys = total_4th_boys + total_5th_boys

    # Calculate the difference between the total number of boys and girls
    difference = total_boys - total_girls

    # Display the difference
    result = difference
    return result

print(solution())