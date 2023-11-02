def solution():
    """At Mrs. Dawson's rose garden, there are 10 rows of roses. In each row, there are 20 roses where 1/2 of these roses are red, 3/5 of the remaining are white and the rest are pink. How many roses at Mrs. Dawson's rose garden are pink?"""
    total_rows = 10
    roses_per_row = 20
    red_percent = 0.5
    white_percent = 0.6
    red_roses = total_rows * roses_per_row * red_percent
    remaining_roses = total_rows * roses_per_row - red_roses
    white_roses = remaining_roses * white_percent
    pink_roses = remaining_roses - white_roses
    result = pink_roses
    return result

print(solution())