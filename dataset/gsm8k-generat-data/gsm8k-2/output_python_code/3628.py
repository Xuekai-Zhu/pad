def solution():
    """Mrs. Amaro has 80 roses in her garden. Three-fourths of her roses are red, one-fourth of the remaining are yellow, and the rest are white. How many of Mrs. Amaro's roses are either red or white?"""
    total_roses = 80
    red_roses = (3/4) * total_roses
    remaining_roses = total_roses - red_roses
    yellow_roses = (1/4) * remaining_roses
    white_roses = total_roses - red_roses - yellow_roses
    red_and_white_roses = red_roses + white_roses
    result = red_and_white_roses
    return result

print(solution())