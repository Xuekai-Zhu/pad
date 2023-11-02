def solution():
    # Define the ratio of sugar to cream cheese
    sugar_to_cc_ratio = 1/4

    # Calculate the amount of cream cheese used
    cream_cheese = 8 * sugar_to_cc_ratio

    # Calculate the amount of vanilla used
    vanilla = cream_cheese / 2

    # Calculate the number of eggs used
    eggs = 2 * vanilla

    result = eggs
    return result

print(solution())