def solution():
    num_cans_before = 22
    num_cans_taken = 6

    # Calculate the number of cans of soda Tim has left
    num_cans_left = num_cans_before - num_cans_taken

    # Calculate the number of cans of soda Tim buys
    num_cans_bought = num_cans_left / 2

    # Calculate the total number of cans of soda Tim has in the end
    num_cans_end = num_cans_left + num_cans_bought
    result = num_cans_end
    return result

print(solution())