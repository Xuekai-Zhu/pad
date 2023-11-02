def solution():
    """Brittany, Alex, and Jamy all share 600 marbles divided between them in the ratio 3:5:7. If Brittany gives Alex half of her marbles, what's the total number of marbles that Alex has?"""
    # Define the ratio of marbles
    ratio = [3, 5, 7]

    # Calculate the total number of parts in the ratio
    total_parts = sum(ratio)

    # Calculate the size of one part of the ratio
    one_part = 600 / total_parts

    # Calculate how many marbles each person gets according to the ratio
    brittany_marbles = ratio[0] * one_part
    alex_marbles = ratio[1] * one_part
    jamy_marbles = ratio[2] * one_part

    # Brittany gives Alex half of her marbles
    brittany_marbles /= 2
    alex_marbles += brittany_marbles

    # Return the total number of marbles Alex has
    result = alex_marbles
    return result

print(solution())