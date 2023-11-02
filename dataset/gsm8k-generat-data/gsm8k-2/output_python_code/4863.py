def solution():
    """Martha is knitting winter clothes for her 3 grandchildren, who are all the same size (identical triplets.) Each set of clothes consists of a woolen hat, a scarf, a sweater, a pair of mittens, and a pair of wooly socks. She can knit a hat in 2 hours. A scarf takes her 3 hours. Each mitten takes her about an hour to knit. A sock takes an hour and a half. Each sweater takes her 6 hours. How long will it take her to knit all the outfits?"""
    hat_time = 2
    scarf_time = 3
    mitten_time = 1
    sock_time = 1.5
    sweater_time = 6
    num_outfits = 3

    total_time = (hat_time + scarf_time + (2 * mitten_time) + (2 * sock_time) + sweater_time) * num_outfits
    result = total_time
    return result

print(solution())