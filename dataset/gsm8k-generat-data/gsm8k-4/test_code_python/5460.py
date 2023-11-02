def solution():
    """Omar buys a 12-ounce cup of coffee every morning on the way to work. On the way to work, he drinks one-quarter of the cup. When he gets to his office, he drinks another half of the cup. He forgets to drink any more of his coffee once he starts working, and when he remembers his coffee, he only drinks 1 ounce of the remaining amount because it is cold. How many ounces will be left in the cup afterward?"""
    # Define the initial size of the cup
    cup_size = 12

    # Calculate the amount of coffee Omar drinks on the way to work
    omar_drinks = cup_size * 0.25

    # Calculate the amount of coffee Omar drinks at his office
    office_drinks = (cup_size - omar_drinks) * 0.5

    # Calculate the amount of coffee left in the cup after he remembers it
    remaining_coffee = cup_size - omar_drinks - office_drinks - 1

    # return the result
    result = remaining_coffee
    return result

print(solution())