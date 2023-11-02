def solution():
    num_bottles = 80
    bottle_value = 0.1
    total_value = 15

    # Calculate the total value of all bottles
    total_bottle_value = num_bottles * bottle_value

    # Calculate the value of all cans
    total_can_value = total_value - total_bottle_value

    # Calculate the number of cans
    num_cans = int(total_can_value / 0.05)
    result = num_cans
    return result

print(solution())