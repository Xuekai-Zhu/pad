def solution():
    num_people = 30
    num_snacks_dropped = 0

    # Calculate the number of times the vending machine fails to drop a snack
    num_no_drop = num_people / 6

    # Calculate the number of times the vending machine accidentally drops two snacks
    num_double_drop = num_people / 10

    # Calculate the total number of snacks dropped
    num_snacks_dropped = num_no_drop + (2 * num_double_drop)

    result = num_snacks_dropped
    return result

print(solution())