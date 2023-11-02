def solution():
    # Calculate the number of slices needed for Brenda and her friends
    num_slices = 10 * 2  # Brenda and 9 friends with 2 slices each

    # Calculate the number of pizzas needed
    num_pizzas = num_slices // 4  # each pizza has 4 slices

    # Round up if there are any leftover slices
    if num_slices % 4 != 0:
        num_pizzas += 1

    result = num_pizzas
    return result

print(solution())