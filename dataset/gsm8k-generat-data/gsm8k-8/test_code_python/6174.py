def solution():
    # Calculate the total amount of flour used for 3 batches of cookies
    total_flour_used = 2 * 3

    # Calculate the remaining flour after making 3 batches of cookies
    remaining_flour = 20 - total_flour_used

    # Calculate the number of batches of cookies that can be made with the remaining flour
    batches_possible = remaining_flour // 2

    result = batches_possible
    return result

print(solution())