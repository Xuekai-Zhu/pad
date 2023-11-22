def solution():
    
    # Define the initial number of cats
    initial_cats = 50

    # Calculate the number of cats carried away by the boats
    cats_carried_away = 4 * 5

    # Calculate the number of cats remaining after the boats carried away
    cats_remaining = initial_cats - cats_carried_away

    # Calculate the number of cats ran after a mouse
    cats_ran_after_mouse = cats_remaining * (3/5)

    # Calculate the number of cats left on the rock
    cats_left = cats_remaining - cats_ran_after_mouse

    # Display the number of cats left on the rock
    result = cats_left
    return result

print(solution())