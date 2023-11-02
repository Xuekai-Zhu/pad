def solution():
    """Omar buys a 12-ounce cup of coffee every morning on the way to work. On the way to work, he drinks one-quarter of the cup. When he gets to his office, he drinks another half of the cup. He forgets to drink any more of his coffee once he starts working, and when he remembers his coffee, he only drinks 1 ounce of the remaining amount because it is cold. How many ounces will be left in the cup afterward?"""
    cup_size = 12
    first_drink = cup_size * (1/4)
    second_drink = cup_size * (1/2)
    remaining_coffee = cup_size - (first_drink + second_drink)
    final_coffee = remaining_coffee - 1
    result = final_coffee
    return result

print(solution())