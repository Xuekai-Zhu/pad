def solution():
    total_pizza = 2
    total_slices = total_pizza * 12
    dean_slices = total_slices / 2
    frank_slices = 3
    sammy_slices = total_slices / 3
    leftover_slices = total_slices - (dean_slices + frank_slices + sammy_slices)
    result = leftover_slices
    return result

print(solution())