def solution():
    
    # Define the number of stories written in the first week
    alani_week1 = 20
    brother_week1 = 40
    margot_week1 = 60

    # Calculate the number of stories written in the second week
    alani_week2 = alani_week1 * 2
    brother_week2 = brother_week1 * 2
    margot_week2 = margot_week1 * 2

    # Calculate the total number of stories written
    total_week1 = alani_week1 + brother_week1 + margot_week1
    total_week2 = alani_week2 + brother_week2 + margot_week2

    # Calculate the total number of stories written altogether
    total_stories = total_week1 + total_week2

    # Display the total number of stories written altogether
    result = total_stories
    return result

print(solution())