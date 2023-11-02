def solution():
    """Lena is making a collage with pictures of all her closest friends and newspaper clippings that are about their interests. She has found three clippings for each friend’s pictures. It takes her six drops of glue to stick down each clipping. Lena has already glued her seven closest friends’ pictures. How many drops of glue will she need for the newspaper clippings for her collage?"""
    clippings_per_friend = 3
    drops_per_clipping = 6
    num_friends = 7
    total_clippings = num_friends * clippings_per_friend
    total_drops = total_clippings * drops_per_clipping
    result = total_drops
    return result

print(solution())