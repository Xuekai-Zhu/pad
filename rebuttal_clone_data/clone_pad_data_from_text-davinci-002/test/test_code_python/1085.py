def solution():
    pizza_slices = 15
    breakfast_slices = 4
    lunch_slices = 2
    snack_slices = 2
    dinner_slices = 5
    slices_left = pizza_slices - breakfast_slices - lunch_slices - snack_slices - dinner_slices
    result = slices_left
    return result

print(solution())