def solution():
    initial_pencils = 50
    manny_pencils = 10
    nilo_pencils = manny_pencils + 10

    # Calculate total number of pencils given away
    total_given = manny_pencils + nilo_pencils

    # Calculate number of pencils Ken kept
    num_kept = initial_pencils - total_given
    result = num_kept
    return result

print(solution())