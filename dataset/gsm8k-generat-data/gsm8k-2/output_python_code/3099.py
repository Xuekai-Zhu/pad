def solution():
    """There are three dogs in the backyard. They like apples, blueberries, and bonnies. The first dog, which likes apples, eats 3 times as many apples as the number of blueberries eaten by the second dog that likes blueberries. The dog that likes blueberries eats 3/4 times as many blueberries as the number of bonnies eaten by the third dog. If the dog that likes bonnies ate 60 of them, calculate the total number of fruits eaten by the three dogs?"""

    bonnie_dog = 60
    blueberry_dog = (3/4) * bonnie_dog
    apple_dog = 3 * blueberry_dog

    total_fruits = apple_dog + blueberry_dog + bonnie_dog

    result = total_fruits
    return result

print(solution())