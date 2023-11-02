def solution():
    """Isabel was helping her mom pick apples from their tree in the front yard. Together they picked 34 apples. They want to make apple pies. Each apple pie needs 4 apples, but the apples have to be ripe. 6 of the apples they picked are not ripe. How many pies can they make?"""
    total_apples = 34
    ripe_apples = total_apples - 6
    pies = ripe_apples // 4
    result = pies
    return result

print(solution())