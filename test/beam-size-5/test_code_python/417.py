def solution():
    
    # Define the initial number of cats
    initial_cats = 50

    # Calculate the number of cats carried away
    carried_cats = 4 * 5

    # Calculate the number of cats remaining after the mouse
    remaining_cats = initial_cats - carried_cats

    # Calculate the number of cats ran after the mouse
    ran_cats = remaining_cats * (3/5)

    # Calculate the number of cats left on the rock
    cats_left = remaining_cats - ran_cats

    # Display the number of cats left on the rock
    result = cats_left
    return result

print(solution())