def solution():
    """Phil and Andre decide to order some pizza. They get a small cheese and a large pepperoni. The small pizza has 8 slices, The large has 14 slices. They have both eaten 9 slices already. How many pieces are left per person?"""
    # Define the number of slices in each pizza
    small_pizza_slices = 8
    large_pizza_slices = 14

    # Define the number of slices eaten by both people
    total_slices_eaten = 9 + 9

    # Calculate the number of slices remaining in each pizza
    small_slices_remaining = small_pizza_slices - 9
    large_slices_remaining = large_pizza_slices - 9

    # Calculate the number of slices remaining per person
    slices_per_person = (small_slices_remaining + large_slices_remaining) / 2

    # return the result
    result = slices_per_person
    return result

print(solution())