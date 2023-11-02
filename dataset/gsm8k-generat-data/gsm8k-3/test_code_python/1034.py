def solution():
    """When Betty makes cheesecake, she sweetens it with a ratio of one part sugar to four parts cream cheese, and she flavors it with one teaspoon of vanilla for every two cups of cream cheese. For every one teaspoon of vanilla, she uses two eggs. She used two cups of sugar in her latest cheesecake. How many eggs did she use?"""
    # Define the ratios and conversions
    SUGAR_TO_CREAMCHEESE = 1/4
    VANILLA_TO_CREAMCHEESE = 1/2
    EGGS_PER_VANILLA = 2

    # Define the amount of sugar used
    sugar_used = 2 # cups

    # Calculate the amount of cream cheese used
    creamcheese_used = sugar_used / SUGAR_TO_CREAMCHEESE

    # Calculate the amount of vanilla used
    vanilla_used = creamcheese_used * VANILLA_TO_CREAMCHEESE

    # Calculate the number of eggs used
    eggs_used = vanilla_used * EGGS_PER_VANILLA

    # Display the number of eggs used
    result = eggs_used
    return result

print(solution())