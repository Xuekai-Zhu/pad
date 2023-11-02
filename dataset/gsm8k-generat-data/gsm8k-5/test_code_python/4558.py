def solution():
    total_slices = 16  # The pizza was cut into 16 slices
    eaten_slices = total_slices / 4  # Yves and his siblings ate one-fourth of the pizza
    remaining_slices = total_slices - eaten_slices  # Calculate the remaining slices after dinner

    remaining_slices = remaining_slices / 4  # Yves ate one-fourth of the remaining slices
    remaining_slices -= 2  # Yves' siblings ate 2 slices each the next day

    result = remaining_slices
    return result

print(solution())