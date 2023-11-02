def solution():
    # Calculate the initial number of apples and plums on the tree
    initial_apples = 180
    initial_plums = initial_apples / 3

    # Calculate the number of fruits Damien picks
    total_fruits = initial_apples + initial_plums
    picked_fruits = 3/5 * total_fruits

    # Calculate the remaining number of apples and plums on the tree
    remaining_fruits = total_fruits - picked_fruits
    remaining_apples = remaining_fruits / 4 * 3
    remaining_plums = remaining_fruits / 4

    # Calculate the total number of remaining fruits on the tree
    total_remaining_fruits = remaining_apples + remaining_plums
    result = total_remaining_fruits
    return result

print(solution())