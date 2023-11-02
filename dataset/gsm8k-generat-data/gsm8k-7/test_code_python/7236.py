def solution():
    num_boys = 14
    num_girls = 10
    num_boys_drop_out = 4
    num_girls_drop_out = 3

    # Calculate the new number of boys and girls after some drop out
    remaining_boys = num_boys - num_boys_drop_out
    remaining_girls = num_girls - num_girls_drop_out

    result = (remaining_boys, remaining_girls)
    return result

print(solution())