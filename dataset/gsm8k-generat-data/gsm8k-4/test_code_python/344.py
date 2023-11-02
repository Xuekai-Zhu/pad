def solution():
    """Archie is playing with his marbles outside. He loses 60% of them into the street. Of the remaining ones, he loses half down a sewer. If he has 20 left, how many did he start with?"""
    # Define the final number of marbles
    final_marbles = 20

    # Calculate the number of marbles lost in the street
    street_loss = final_marbles / 0.4 - final_marbles

    # Calculate the number of marbles lost down the sewer
    sewer_loss = street_loss / 2

    # Calculate the initial number of marbles
    initial_marbles = final_marbles + street_loss + sewer_loss

    result = initial_marbles
    return result

print(solution())