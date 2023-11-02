def solution():
    friends = 7  # Lena has 7 closest friends
    clippings_per_friend = 3  # Lena has 3 clippings for each friend's pictures
    glue_per_clipping = 6  # Lena needs 6 drops of glue for each clipping

    # Calculate the total number of clippings in the collage
    total_clippings = friends * clippings_per_friend

    # Calculate the total number of drops of glue needed for the clippings
    total_glue = total_clippings * glue_per_clipping
    result = total_glue
    return result

print(solution())