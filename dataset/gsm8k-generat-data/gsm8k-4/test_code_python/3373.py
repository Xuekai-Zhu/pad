def solution():
    """Shonda is throwing an Easter egg hunt for her 2 kids and their 10 friends. She is also supplying enough eggs for herself and the 7 other adults there to find eggs as well. If there are 15 Easter egg baskets for everyone to share and each ends up holding 12 Easter eggs, when they equally distribute all of the Easter eggs to everyone, how many eggs does each person get?"""
    # Define the number of people attending the Easter egg hunt
    total_people = 2 + 10 + 1 + 7

    # Define the number of Easter egg baskets
    egg_baskets = 15

    # Define the number of eggs per basket
    eggs_per_basket = 12

    # Calculate the total number of eggs
    total_eggs = egg_baskets * eggs_per_basket

    # Calculate the number of eggs each person gets
    eggs_per_person = total_eggs // total_people

    # return the result
    result = eggs_per_person
    return result

print(solution())