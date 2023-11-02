def solution():
    """At Mrs. Dawson's rose garden, there are 10 rows of roses. In each row, there are 20 roses where 1/2 of these roses are red, 3/5 of the remaining are white and the rest are pink. How many roses at Mrs. Dawson's rose garden are pink?"""
    # Define the number of rows and roses per row
    rows = 10
    roses_per_row = 20

    # Calculate the total number of roses
    total_roses = rows * roses_per_row

    # Calculate the number of red roses
    red_roses = total_roses / 2

    # Calculate the number of remaining roses
    remaining_roses = total_roses - red_roses

    # Calculate the number of white roses
    white_roses = remaining_roses * 3/5

    # Calculate the number of pink roses
    pink_roses = total_roses - red_roses - white_roses

    result = pink_roses
    return result

print(solution())