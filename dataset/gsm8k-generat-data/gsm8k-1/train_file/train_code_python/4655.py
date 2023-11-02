def solution():
    """Mary bought 14 apples, 9 oranges, and 6 blueberries. Mary ate 1 of each. How many fruits in total does she have left?"""
    apples = 14
    oranges = 9
    blueberries = 6
    fruits_eaten = 3
    total_fruits_left = (apples + oranges + blueberries) - fruits_eaten
    result = total_fruits_left
    return result

print(solution())