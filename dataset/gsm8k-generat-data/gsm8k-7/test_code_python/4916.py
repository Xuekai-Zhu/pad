def solution():
    num_apples = 7
    num_oranges = 8
    num_mangoes = 15

    # Remove 2 apples from the bag
    num_apples -= 2

    # Determine the number of oranges to remove
    num_oranges_to_remove = 2 * 2  # twice as many oranges as apples
    # Check if there are enough oranges in the bag to remove
    if num_oranges_to_remove > num_oranges:
        num_oranges_to_remove = num_oranges
    # Remove the oranges from the bag
    num_oranges -= num_oranges_to_remove

    # Determine the number of mangoes to remove
    num_mangoes_to_remove = int(2/3 * num_mangoes)
    # Check if there are enough mangoes in the bag to remove
    if num_mangoes_to_remove > num_mangoes:
        num_mangoes_to_remove = num_mangoes
    # Remove the mangoes from the bag
    num_mangoes -= num_mangoes_to_remove

    # Calculate the remaining fruits in the bag
    num_fruits = num_apples + num_oranges + num_mangoes
    result = num_fruits
    return result

print(solution())