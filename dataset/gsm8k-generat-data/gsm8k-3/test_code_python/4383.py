def solution():
    """Lena is making a collage with pictures of all her closest friends and newspaper clippings that are about their interests. She has found three clippings for each friend’s pictures. It takes her six drops of glue to stick down each clipping. Lena has already glued her seven closest friends’ pictures. How many drops of glue will she need for the newspaper clippings for her collage?"""
    # Define the number of clippings per friend
    CLIPPINGS_PER_FRIEND = 3

    # Define the number of drops of glue per clipping
    DROPS_PER_CLIPPING = 6

    # Define the number of friends in the collage
    NUM_FRIENDS = 7

    # Calculate the total number of clippings
    total_clippings = NUM_FRIENDS * CLIPPINGS_PER_FRIEND

    # Calculate the total number of drops of glue needed
    total_glue = total_clippings * DROPS_PER_CLIPPING

    # Display the total number of drops of glue needed
    result = total_glue
    return result

print(solution())