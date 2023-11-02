def solution():
    """Lard decides to share a pizza with his friend Jelly. He takes a whole, uncut pepperoni pizza and cuts it in half. He then cuts these halves in half and gives one of the slices to Jelly. Assuming the pizza started with 40 evenly spread slices of pepperoni, how many slices of it are on the slice Lard gives Jelly if 1 of them falls off the slice when Lard picks it up?"""
    # Define the initial number of pizza slices
    pizza_slices = 40

    # Cut the pizza in half, then in half again
    pizza_slices = pizza_slices // 4

    # Give one slice to Jelly and subtract one that falls off
    jelly_slice = pizza_slices // 2 - 1

    # Return the number of slices on the slice given to Jelly
    result = jelly_slice
    return result

print(solution())