def solution():
    pepperoni_slices = 16
    cheese_slices = 16
    total_slices = pepperoni_slices + cheese_slices
    slices_eaten = total_slices - 1
    cheese_slices_left = 7
    pepperoni_slices_eaten = slices_eaten - cheese_slices_left
    result = pepperoni_slices_eaten / 3
    return result

print(solution())