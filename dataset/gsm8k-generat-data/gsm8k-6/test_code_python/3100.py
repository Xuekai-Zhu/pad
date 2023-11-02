def solution():
    # Find the number of blueberries eaten by the second dog
    blueberries_second_dog = 4/3 * 60  # the third dog eats 60 bonnies and the second dog eats 3/4 times as many blueberries

    # Find the number of apples eaten by the first dog
    apples_first_dog = 3 * blueberries_second_dog  # the first dog eats 3 times as many apples as the second dog eats blueberries

    # Calculate the total number of fruits eaten by the dogs
    total_fruits = apples_first_dog + blueberries_second_dog + 60  # the third dog eats 60 bonnies, the second dog eats blueberries and the first dog eats apples
    result = total_fruits
    return result.

print(solution())