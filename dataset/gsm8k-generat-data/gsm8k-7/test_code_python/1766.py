def solution():
    num_necklaces_1st_machine = 45
    num_necklaces_2nd_machine = 2.4 * num_necklaces_1st_machine

    # Calculate the total number of necklaces made on Sunday
    total_necklaces = num_necklaces_1st_machine + num_necklaces_2nd_machine
    result = total_necklaces
    return result

print(solution())