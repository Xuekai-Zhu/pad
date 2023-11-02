def solution():
    tall_cupboard = 20  # The tall cupboard can hold 20 glasses
    wide_cupboard = 2 * tall_cupboard  # The wide cupboard can hold twice as many
    narrow_cupboard = 15 * 2  # The narrow cupboard has 2 shelves, each holding 15 glasses
    broken_shelf = narrow_cupboard // 2  # Damien broke one shelf in the narrow cupboard

    # Calculate the total number of glasses that can be displayed
    total_display = tall_cupboard + wide_cupboard + narrow_cupboard - broken_shelf
    result = total_display
    return result

print(solution())