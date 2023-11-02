def solution():
    
    # Define the height of the beanstalk in the first week
    week1_height = 3

    # Calculate the height of the beanstalk in the second week
    week2_height = week1_height * 2

    # Calculate the height of the beanstalk in the third week
    week3_height = week2_height + 4

    # Calculate the total height of the beanstalk after 3 weeks
    total_height = week1_height + week2_height + week3_height

    # Display the total height
    result = total_height
    return result

print(solution())