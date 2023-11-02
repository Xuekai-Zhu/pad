def solution():
    pencils_per_box = 12  # Each box of pencils has 12 pencils
    total_pencils = 2 * pencils_per_box  # Steve has 2 boxes of pencils

    # Calculate the number of pencils Steve gave to Matt
    pencils_to_matt = 6 + 3  # Matt got 3 more pencils than Lauren
    pencils_to_lauren = 6

    # Subtract the pencils given away from the total number of pencils
    pencils_left = total_pencils - pencils_to_matt - pencils_to_lauren
    result = pencils_left
    return result

print(solution())