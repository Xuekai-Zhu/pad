def solution():
    # Calculate the number of blueberries eaten by the second dog
    blueberries_second_dog = 4/3 * 60

    # Calculate the number of apples eaten by the first dog
    apples_first_dog = 3 * blueberries_second_dog

    # Calculate the number of fruits eaten by all three dogs
    fruits_total = apples_first_dog + blueberries_second_dog + 60
    result = fruits_total
    return result

print(solution())