def solution():
    """Lena is making a collage with pictures of all her closest friends and newspaper clippings that are about their interests. She has found three clippings for each friend’s pictures. It takes her six drops of glue to stick down each clipping. Lena has already glued her seven closest friends’ pictures. How many drops of glue will she need for the newspaper clippings for her collage?"""
    # Define the number of friends and clippings per friend
    friends = 7
    clippings_per_friend = 3

    # Calculate the total number of clippings
    total_clippings = friends * clippings_per_friend

    # Calculate the total number of drops of glue needed
    drops_of_glue = total_clippings * 6

    # return the result
    result = drops_of_glue
    return result

print(solution())