def solution():
    # Calculate the amount of cream cheese used
    cream_cheese = 4 * 2  # 4 parts cream cheese for each part of sugar, and 2 cups of sugar used

    # Calculate the amount of vanilla used
    vanilla = (1/2) * cream_cheese  # one teaspoon of vanilla for every two cups of cream cheese

    # Calculate the number of eggs used
    eggs = 2 * vanilla  # two eggs for every one teaspoon of vanilla

    result = eggs
    return result

print(solution())