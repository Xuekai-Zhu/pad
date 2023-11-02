def solution():
    # Calculate the total number of pencils Steve has
    total_pencils = 2 * 12

    # Calculate the number of pencils Steve gave to Matt
    matt_pencils = 6 + 3

    # Calculate the total number of pencils Steve gave away
    total_given = 6 + matt_pencils

    # Calculate the number of pencils Steve has left
    pencils_left = total_pencils - total_given
    result = pencils_left
    return result

print(solution())