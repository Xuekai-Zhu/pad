def solution():
    """Mary bought 14 apples, 9 oranges, and 6 blueberries. Mary ate 1 of each. How many fruits in total does she have left?"""
    total_fruits = 14 + 9 + 6
    fruits_eaten = 3
    fruits_left = total_fruits - fruits_eaten
    result = fruits_left
    return result

print(solution())