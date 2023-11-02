def solution():
    """Albert has three times as many marbles as Angela. Angela has 8 more than Allison, who has 28 marbles. How many marbles do Albert and Allison have?"""
    # Define the number of marbles that Allison has
    allison_marbles = 28

    # Calculate the number of marbles that Angela has
    angela_marbles = allison_marbles + 8

    # Calculate the number of marbles that Albert has
    albert_marbles = angela_marbles * 3

    # Calculate the total number of marbles that Albert and Allison have
    total_marbles = albert_marbles + allison_marbles

    # Display the total number of marbles
    result = total_marbles
    return result

print(solution())