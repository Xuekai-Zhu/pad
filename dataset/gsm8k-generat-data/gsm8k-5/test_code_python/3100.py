def solution():
    bonnie_eaten = 60  # The dog that likes bonnies ate 60 of them
    blueberry_eaten = (4/3) * bonnie_eaten  # The dog that likes blueberries eats 3/4 times as many blueberries as the number of bonnies eaten
    apple_eaten = 3 * blueberry_eaten  # The first dog, which likes apples, eats 3 times as many apples as the number of blueberries eaten by the second dog

    # Calculate the total number of fruits eaten by the three dogs
    total_fruits = apple_eaten + blueberry_eaten + bonnie_eaten
    result = total_fruits
    return result

print(solution())