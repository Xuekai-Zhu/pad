def solution():
    # Define the number of friends and clippings per friend
    num_friends = 7
    clippings_per_friend = 3

    # Calculate the total number of clippings
    total_clippings = num_friends * clippings_per_friend

    # Calculate the total number of glue drops needed
    glue_drops_per_clipping = 6
    total_glue_drops = total_clippings * glue_drops_per_clipping

    result = total_glue_drops
    return result

print(solution())