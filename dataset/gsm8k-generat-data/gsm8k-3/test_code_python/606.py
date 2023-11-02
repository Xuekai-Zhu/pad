def solution():
    """In a big box, there are marbles in 4 colors. Inside, there are 20 red marbles.  There are three times more green marbles than red.  Yellow marbles make up 20% of the green marbles. How many marbles are of a different color if the total of all marbles in the box is three times more than the number of green marbles?"""
    # Define the number of red marbles
    red_marbles = 20

    # Calculate the number of green marbles
    green_marbles = 3 * red_marbles

    # Calculate the number of yellow marbles
    yellow_marbles = int(0.2 * green_marbles)

    # Calculate the total number of marbles
    total_marbles = 4 * (red_marbles + green_marbles + yellow_marbles)

    # Calculate the number of marbles of a different color
    different_marbles = total_marbles - green_marbles

    # Display the number of marbles of a different color
    result = different_marbles
    return result

print(solution())