def solution():
    """Sunnyvale School was having a picnic. They wanted to make fruit punch. They had 4.5 liters of orange punch. They had twice as much cherry punch as orange punch and 1.5 liters less of apple juice than cherry punch. When they combined all of the fruit juices together, how many liters of fruit punch did they have?"""
    # Define the amount of orange punch
    orange_punch = 4.5

    # Define the amount of cherry punch (twice the amount of orange punch)
    cherry_punch = orange_punch * 2

    # Define the amount of apple juice (1.5 less than the amount of cherry punch)
    apple_juice = cherry_punch - 1.5

    # Calculate the total amount of fruit punch
    total_punch = orange_punch + cherry_punch + apple_juice

    # return the result
    result = total_punch
    return result

print(solution())