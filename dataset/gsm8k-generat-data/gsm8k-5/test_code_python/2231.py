def solution():
    couple_slices = 3 * 2  # The couple wants 3 slices each, and there are 2 people in the couple
    children_slices = 6  # There are 6 children who each want 1 slice
    total_slices = couple_slices + children_slices  # Calculate the total number of slices needed
    pizzas = (total_slices // 4) + 1 # Divide the total number of slices by 4 (rounding up to the nearest integer)
                                        #(to account for the possibility that they need an extra pizza)
    result = pizzas
    return result

print(solution())