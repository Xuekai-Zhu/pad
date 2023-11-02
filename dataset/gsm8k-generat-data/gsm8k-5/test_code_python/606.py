def solution():
    red_marbles = 20  # There are 20 red marbles in the box
    green_marbles = 3 * red_marbles  # There are three times more green marbles than red
    yellow_marbles = 0.2 * green_marbles  # Yellow marbles make up 20% of the green marbles
    total_marbles = 3 * green_marbles  # The total number of marbles in the box is three times more than the number of green marbles

    # Calculate the number of marbles that are not red, green, or yellow
    other_marbles = total_marbles - (red_marbles + green_marbles + yellow_marbles)

    result = other_marbles
    return result

print(solution())