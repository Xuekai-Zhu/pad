def solution():
    """Sunnyvale School was having a picnic. They wanted to make fruit punch. They had 4.5 liters of orange punch. They had twice as much cherry punch as orange punch and 1.5 liters less of apple juice than cherry punch. When they combined all of the fruit juices together, how many liters of fruit punch did they have?"""
    orange_punch = 4.5
    cherry_punch = 2 * orange_punch
    apple_juice = cherry_punch - 1.5
    total_punch = orange_punch + cherry_punch + apple_juice
    result = total_punch
    return result

print(solution())