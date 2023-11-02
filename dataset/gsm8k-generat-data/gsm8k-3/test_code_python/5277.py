def solution():
    """Isabel was helping her mom pick apples from their tree in the front yard.  Together they picked 34 apples.  They want to make apple pies.  Each apple pie needs 4 apples, but the apples have to be ripe.  6 of the apples they picked are not ripe.  How many pies can they make?"""
    # Calculate the number of ripe apples
    ripe_apples = 34 - 6

    # Calculate the number of pies they can make
    num_pies = ripe_apples // 4

    # Display the number of pies they can make
    result = num_pies
    return result

print(solution())