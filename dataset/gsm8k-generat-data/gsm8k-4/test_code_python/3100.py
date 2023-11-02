def solution():
    """There are three dogs in the backyard. They like apples, blueberries, and bonnies. The first dog, which likes apples, eats 3 times as many apples as the number of blueberries eaten by the second dog that likes blueberries. The dog that likes blueberries eats 3/4 times as many blueberries as the number of bonnies eaten by the third dog. If the dog that likes bonnies ate 60 of them, calculate the total number of fruits eaten by the three dogs?"""
    # Define the number of bonnies eaten by the third dog
    bonnie_count = 60

    # Calculate the number of blueberries eaten by the second dog
    blueberry_count = bonnie_count / (3/4)

    # Calculate the number of apples eaten by the first dog
    apple_count = blueberry_count * 3

    # Calculate the total number of fruits eaten by the three dogs
    total_count = apple_count + blueberry_count + bonnie_count

    result = total_count
    return result

print(solution())