def solution():
    """Yves and his siblings ordered pizza and asked to have it cut into 16 slices. During dinner time, they only ate one-fourth of it. The next day, Yves ate one-fourth of the remaining pizza. Then his two siblings ate 2 slices each. How many slices of pizza were left?"""
    total_slices = 16
    initial_slices_eaten = total_slices / 4
    remaining_slices = total_slices - initial_slices_eaten
    yves_slices = remaining_slices / 4
    remaining_slices -= yves_slices
    siblings_slices = 2 * 2
    remaining_slices -= siblings_slices
    result = remaining_slices
    return result

print(solution())