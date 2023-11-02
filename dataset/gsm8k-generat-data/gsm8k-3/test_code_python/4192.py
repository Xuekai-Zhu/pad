def solution():
    """Susan loves chairs. In her house there are red chairs, yellow chairs, and blue chairs. There are 5 red chairs. There are 4 times as many yellow chairs as red chairs, and there are 2 fewer blue chairs than yellow chairs. How many chairs are there in Susan's house?"""
    # Define the number of red chairs
    red_chairs = 5

    # Calculate the number of yellow chairs
    yellow_chairs = 4 * red_chairs

    # Calculate the number of blue chairs
    blue_chairs = yellow_chairs - 2

    # Calculate the total number of chairs
    total_chairs = red_chairs + yellow_chairs + blue_chairs

    # Display the total number of chairs in Susan's house
    result = total_chairs
    return result

print(solution())