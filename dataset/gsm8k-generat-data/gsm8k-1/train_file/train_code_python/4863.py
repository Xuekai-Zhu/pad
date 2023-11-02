def solution():
    """Martha is knitting winter clothes for her 3 grandchildren, who are all the same size (identical triplets.) Each set of clothes consists of a woolen hat, a scarf, a sweater, a pair of mittens, and a pair of wooly socks. She can knit a hat in 2 hours. A scarf takes her 3 hours. Each mitten takes her about an hour to knit. A sock takes an hour and a half. Each sweater takes her 6 hours. How long will it take her to knit all the outfits?"""
    hats_hours = 2
    scarfs_hours = 3
    mittens_hours = 1
    socks_hours = 1.5
    sweaters_hours = 6
    outfits_per_grandchild = 5
    grandchild_count = 3
    total_outfits = outfits_per_grandchild * grandchild_count
    total_hours = (hats_hours + scarfs_hours + (mittens_hours * 2) +
                   (socks_hours * 2) + sweaters_hours) * total_outfits
    result = total_hours
    return result

print(solution())