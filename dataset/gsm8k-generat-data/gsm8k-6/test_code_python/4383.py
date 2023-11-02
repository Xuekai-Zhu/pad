def solution():
    # Calculate the total number of clippings
    total_clippings = 7 * 3  # Lena has 3 clippings for each of her 7 closest friends

    # Calculate the total number of drops of glue needed
    total_glue_drops = total_clippings * 6  # it takes 6 drops of glue to stick down each clipping

    result = total_glue_drops
    return result

print(solution())