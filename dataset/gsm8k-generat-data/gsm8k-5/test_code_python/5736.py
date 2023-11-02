def solution():
    pencils_per_box = 14  # Each box contains 14 pencils
    total_pencils = pencils_per_box * 2  # Ashton has two boxes of pencils
    pencils_given_away = 6  # Ashton gave away 6 pencils

    # Calculate the number of pencils Ashton has left
    pencils_left = total_pencils - pencils_given_away
    result = pencils_left
    return result

print(solution())