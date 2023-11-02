def solution():
    batch_size = 48
    sold_first_batch = 37
    sold_second_batch = 52
    sold_third_batch = 49

    # Calculate the total number of baguettes made
    total_baguettes = 3 * batch_size

    # Calculate the number of baguettes sold
    total_sold = sold_first_batch + sold_second_batch + sold_third_batch

    # Calculate the number of baguettes left
    num_left = total_baguettes - total_sold
    result = num_left
    return result

print(solution())