def solution():
    total_marbles = 215
    difference = 55

    # Calculate the total number of marbles owned by Amon and Rhonda together
    # If Amon has 55 more marbles than Rhonda, and they have a total of 215 marbles,
    # then we can represent Amon's number of marbles as Rhonda's number plus 55.
    # So, Rhonda has x marbles and Amon has x + 55 marbles, and together they have 215 marbles:
    #   x + (x + 55) = 215
    # Simplifying this equation:
    #   2x + 55 = 215
    #   2x = 160
    #   x = 80
    # Therefore, Rhonda has 80 marbles.

    rhonda_marbles = (total_marbles - difference) / 2
    result = rhonda_marbles
    return result

print(solution())