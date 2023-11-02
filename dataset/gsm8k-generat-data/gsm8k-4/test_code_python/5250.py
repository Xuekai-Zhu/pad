def solution():
    """7 out of 40 people in a cafeteria are wearing checkered shirts. The rest of the people are wearing vertical stripes and horizontal stripes. The number of people wearing horizontal stripes is 4 times as many as the people wearing checkered shirts. How many people are wearing vertical stripes?"""
    # Define the total number of people in the cafeteria and the number of people wearing checkered shirts
    total_people = 40
    checkered_shirts = 7

    # Calculate the number of people wearing horizontal stripes
    horizontal_stripes = 4 * checkered_shirts

    # Calculate the number of people wearing vertical stripes
    vertical_stripes = total_people - checkered_shirts - horizontal_stripes

    # Return the result
    result = vertical_stripes
    return result

print(solution())