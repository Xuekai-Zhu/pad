def solution():
    """A 76-star flag has three rows of 8 stars, two rows of 6 stars and the rest are 5-star rows. How many rows of 5 stars are there altogether on the flag?"""
    total_stars = 76
    star_rows = [(3, 8), (2, 6)]
    star_count = sum([rows * count for rows, count in star_rows])
    five_star_rows = (total_stars - star_count) / 5
    result = five_star_rows
    return result

print(solution())