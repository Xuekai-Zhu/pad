def solution():
    """At Mrs. Dawson's rose garden, there are 10 rows of roses. In each row, there are 20 roses where 1/2 of these roses are red, 3/5 of the remaining are white and the rest are pink. How many roses at Mrs. Dawson's rose garden are pink?"""
    rows = 10
    roses_per_row = 20
    red_ratio = 1/2
    white_ratio = 3/5
    pink_ratio = 1 - red_ratio - white_ratio
    total_roses = rows * roses_per_row
    red_roses = total_roses * red_ratio
    remaining_roses = total_roses - red_roses
    white_roses = remaining_roses * white_ratio
    pink_roses = remaining_roses - white_roses
    result = pink_roses
    return result

print(solution())