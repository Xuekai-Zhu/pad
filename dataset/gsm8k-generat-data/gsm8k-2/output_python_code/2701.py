def solution():
    """Stephen ordered 2 large pizzas, both cut into 12 slices. He ate 25% of the pizza. His friend Pete ate 50% of the remaining pizza. How many slices are left over?"""
    total_slices = 2 * 12
    stephen_slices_eaten = int(total_slices * 0.25)
    remaining_slices = total_slices - stephen_slices_eaten
    pete_slices_eaten = int(remaining_slices * 0.5)
    total_slices_left = remaining_slices - pete_slices_eaten
    result = total_slices_left
    return result

print(solution())