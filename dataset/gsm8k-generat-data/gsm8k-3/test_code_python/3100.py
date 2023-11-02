def solution():
    """There are three dogs in the backyard. They like apples, blueberries, and bonnies. The first dog, which likes apples, eats 3 times as many apples as the number of blueberries eaten by the second dog that likes blueberries. The dog that likes blueberries eats 3/4 times as many blueberries as the number of bonnies eaten by the third dog. If the dog that likes bonnies ate 60 of them, calculate the total number of fruits eaten by the three dogs?"""
    # Calculate the number of blueberries eaten by the second dog
    blueberries_2 = 3/4 * 60

    # Calculate the number of apples eaten by the first dog
    apples_1 = 3 * blueberries_2

    # Calculate the total number of fruits eaten by the three dogs
    total_fruits = apples_1 + blueberries_2 + 60

    # Display the total number of fruits
    result = total_fruits
    return result

print(solution())