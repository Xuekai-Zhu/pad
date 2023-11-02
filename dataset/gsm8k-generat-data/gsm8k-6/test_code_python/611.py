def solution():
    # Calculate the number of slices on the slice Lard gives Jelly
    slices_on_half_pizza = 40 / 2  # Half of the pizza contains 20 slices of pepperoni
    slices_on_quarter_pizza = slices_on_half_pizza / 2  # Each half is then divided into 10 slices of pepperoni
    slices_on_jelly_slice = slices_on_quarter_pizza - 1  # 1 slice of pepperoni falls off the slice when Lard picks it up
    result = slices_on_jelly_slice
    return result

print(solution())