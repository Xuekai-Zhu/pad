def solution():
    """Martha is knitting winter clothes for her 3 grandchildren, who are all the same size (identical triplets.) Each set of clothes consists of a woolen hat, a scarf, a sweater, a pair of mittens, and a pair of wooly socks. She can knit a hat in 2 hours. A scarf takes her 3 hours. Each mitten takes her about an hour to knit. A sock takes an hour and a half. Each sweater takes her 6 hours. How long will it take her to knit all the outfits?"""
    # Define the time to knit each item
    hat_time = 2
    scarf_time = 3
    mitten_time = 1
    sock_time = 1.5
    sweater_time = 6

    # Calculate the total knitting time for all items in one set
    set_time = hat_time + scarf_time + (2 * mitten_time) + (2 * sock_time) + sweater_time

    # Calculate the total knitting time for all sets
    total_time = set_time * 3

    # Return the result
    result = total_time
    return result

print(solution())