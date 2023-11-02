def solution():
    total_slices = 2 * 12  # 2 pizzas with 12 slices each
    num_slices_bob_ate = 0.5 * 12  # Bob had half of a pizza, or 6 slices
    num_slices_tom_ate = (1/3) * 12  # Tom had one-third of a pizza, or 4 slices
    num_slices_sally_ate = (1/6) * 12  # Sally had one-sixth of a pizza, or 2 slices
    num_slices_jerry_ate = 0.25 * 12  # Jerry had a quarter of a pizza, or 3 slices

    # Calculate the total number of slices eaten
    total_slices_eaten = num_slices_bob_ate + num_slices_tom_ate + num_slices_sally_ate + num_slices_jerry_ate

    # Calculate the number of slices left over
    num_slices_left_over = total_slices - total_slices_eaten
    result = num_slices_left_over
    return result

print(solution())