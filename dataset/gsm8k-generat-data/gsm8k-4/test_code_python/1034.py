def solution():
    """When Betty makes cheesecake, she sweetens it with a ratio of one part sugar to four parts cream cheese, and she flavors it with one teaspoon of vanilla for every two cups of cream cheese. For every one teaspoon of vanilla, she uses two eggs. She used two cups of sugar in her latest cheesecake. How many eggs did she use?"""
    # Define the ratio of sugar to cream cheese
    sugar_to_cheese = 1 / 4

    # Calculate the amount of cream cheese used
    cheese = 2 / sugar_to_cheese

    # Calculate the amount of vanilla used
    vanilla = cheese / 2

    # Calculate the number of eggs used
    eggs = 2 * vanilla

    # Round up to the nearest whole number since you cannot use partial eggs
    eggs = round(eggs)

    # return the result
    result = eggs
    return result

print(solution())