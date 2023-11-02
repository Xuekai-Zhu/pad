def solution():
    # Calculate the number of years the tree has been growing
    years_growing = 9 - 4  # Lydia planted the tree when she was 4 years old and is now 9 years old

    # Calculate the number of years left until the tree bears fruit
    years_left_to_bear_fruit = 7 - years_growing

    # Calculate the age Lydia will be when she gets to eat an apple from her tree for the first time
    age_when_tree_bears_fruit = 9 + years_left_to_bear_fruit
    result = age_when_tree_bears_fruit
    return result

print(solution())