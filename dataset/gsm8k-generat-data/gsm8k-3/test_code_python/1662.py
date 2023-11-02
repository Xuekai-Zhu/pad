def solution():
    """A tomato plant has 100 tomatoes. Jane picks 1/4 of that number for use in their house. After a week, she goes back and picks 20 more tomatoes, and the following week picks twice that number. What's the total number of fruits remaining on the tomato plant?"""
    # Define the initial number of tomatoes on the plant
    initial_tomatoes = 100

    # Calculate the number of tomatoes Jane picks in the first week
    first_week_picks = initial_tomatoes // 4

    # Calculate the number of tomatoes remaining after the first week
    remaining_tomatoes = initial_tomatoes - first_week_picks

    # Calculate the number of tomatoes Jane picks in the second week
    second_week_picks = 20

    # Calculate the number of tomatoes remaining after the second week
    remaining_tomatoes -= second_week_picks

    # Calculate the number of tomatoes Jane picks in the third week
    third_week_picks = second_week_picks * 2

    # Calculate the final number of tomatoes remaining
    final_tomatoes = remaining_tomatoes - third_week_picks

    # Display the final number of tomatoes remaining
    result = final_tomatoes
    return result

print(solution())