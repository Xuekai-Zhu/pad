def solution():
    num_start_pencils = 20
    num_misplaced_pencils = 7
    num_broken_pencils = 3
    num_found_pencils = 4
    num_bought_pencils = 2

    # Calculate the total number of pencils that Autumn has after the first month
    num_remaining_pencils = num_start_pencils - num_misplaced_pencils - num_broken_pencils + num_found_pencils + num_bought_pencils

    result = num_remaining_pencils
    return result

print(solution())