def solution():
    """There are three dogs in the backyard. They like apples, blueberries, and bonnies. The first dog, which likes apples, eats 3 times as many apples as the number of blueberries eaten by the second dog that likes blueberries. The dog that likes blueberries eats 3/4 times as many blueberries as the number of bonnies eaten by the third dog. If the dog that likes bonnies ate 60 of them, calculate the total number of fruits eaten by the three dogs?"""
    bonnies_eaten = 60
    blueberries_eaten = (3/4) * bonnies_eaten
    apples_eaten = 3 * blueberries_eaten
    total_fruits_eaten = bonnies_eaten + blueberries_eaten + apples_eaten
    result = total_fruits_eaten
    return result

print(solution())