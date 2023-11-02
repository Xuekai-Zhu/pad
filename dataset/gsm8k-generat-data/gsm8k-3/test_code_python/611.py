def solution():
    """Lard decides to share a pizza with his friend Jelly.  He takes a whole, uncut pepperoni pizza and cuts it in half.  He then cuts these halves in half and gives one of the slices to Jelly.  Assuming the pizza started with 40 evenly spread slices of pepperoni, how many slices of it are on the slice Lard gives Jelly if 1 of them falls off the slice when Lard picks it up?"""
    # Calculate the total number of slices after each cut
    num_slices = [40, 20, 10, 5]

    # Determine the number of slices on the slice Lard gives Jelly
    jelly_slice = num_slices[3] - 1

    # Display the number of pepperoni slices on the slice Lard gives Jelly
    result = jelly_slice
    return result

print(solution())