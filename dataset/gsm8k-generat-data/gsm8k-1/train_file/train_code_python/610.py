def solution():
    """Lard decides to share a pizza with his friend Jelly. He takes a whole, uncut pepperoni pizza and cuts it in half. He then cuts these halves in half and gives one of the slices to Jelly. Assuming the pizza started with 40 evenly spread slices of pepperoni, how many slices of it are on the slice Lard gives Jelly if 1 of them falls off the slice when Lard picks it up?"""
    slices_per_pizza = 40
    slices_per_quarter = slices_per_pizza / 4
    slices_given_to_jelly = slices_per_quarter - 1
    result = slices_given_to_jelly
    return result

print(solution())