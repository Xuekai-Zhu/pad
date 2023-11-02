def solution():
    """Jennifer has ten pears, 20 oranges, and twice as many apples as pears. If she gives her sister two of each fruit, how many fruits does she have left?"""
    pears = 10
    oranges = 20
    apples = 2 * pears
    total_fruits = pears + oranges + apples
    fruits_given_away = 2 * 3  # two of each fruit given away
    fruits_left = total_fruits - fruits_given_away
    result = fruits_left
    return result

print(solution())