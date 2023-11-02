def solution():
    initial_number = 20
    part_one_loss = initial_number * 0.6
    part_two_loss = initial_number * 0.5
    total_loss = part_one_loss + part_two_loss
    final_number = initial_number - total_loss
    result = final_number

    return result

print(solution())