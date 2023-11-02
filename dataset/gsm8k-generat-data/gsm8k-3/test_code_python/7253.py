def solution():
    """In Rodrigo's classroom in the morning there are red chairs, yellow chairs, and blue chairs. There are 4 red chairs. There are 2 times as many yellow chairs as red chairs, and there are 2 fewer blue chairs than yellow chairs. In the afternoon, Lisa borrows 3 chairs. How many chairs are left in Rodrigo's classroom?"""
    # Define the number of red chairs
    red_chairs = 4

    # Define the number of yellow chairs
    yellow_chairs = 2 * red_chairs

    # Define the number of blue chairs
    blue_chairs = yellow_chairs - 2

    # Calculate the total number of chairs in the morning
    total_chairs_morning = red_chairs + yellow_chairs + blue_chairs

    # Calculate the total number of chairs in the afternoon
    total_chairs_afternoon = total_chairs_morning - 3

    # Display the number of chairs left in the classroom
    result = total_chairs_afternoon
    return result

print(solution())