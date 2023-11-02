def solution():
    """Sunnyvale School was having a picnic. They wanted to make fruit punch. They had 4.5 liters of orange punch. They had twice as much cherry punch as orange punch and 1.5 liters less of apple juice than cherry punch. When they combined all of the fruit juices together, how many liters of fruit punch did they have?"""
    # Define the amount of orange punch
    orange_punch = 4.5

    # Calculate the amount of cherry punch
    cherry_punch = orange_punch * 2

    # Calculate the amount of apple juice
    apple_juice = cherry_punch - 1.5

    # Calculate the total amount of fruit punch
    total_punch = orange_punch + cherry_punch + apple_juice

    # Display the total amount of fruit punch
    result = total_punch
    return result

print(solution())