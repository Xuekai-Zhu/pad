def solution():
    """Lena is making a collage with pictures of all her closest friends and newspaper clippings that are about their interests. She has found three clippings for each friend’s pictures. It takes her six drops of glue to stick down each clipping. Lena has already glued her seven closest friends’ pictures. How many drops of glue will she need for the newspaper clippings for her collage?"""
    friends = 7
    clippings_per_friend = 3
    glue_per_clipping = 6
    total_clippings = friends * clippings_per_friend
    total_glue = total_clippings * glue_per_clipping
    result = total_glue
    return result

print(solution())