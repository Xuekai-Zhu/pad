def solution():
    """At Mrs. Dawson's rose garden, there are 10 rows of roses. In each row, there are 20 roses where 1/2 of these roses are red, 3/5 of the remaining are white and the rest are pink. How many roses at Mrs. Dawson's rose garden are pink?"""
    # Define the number of rows and roses per row
    ROWS = 10
    ROSES_PER_ROW = 20

    # Calculate the number of red roses per row
    red_roses_per_row = ROSES_PER_ROW / 2

    # Calculate the number of remaining roses after red roses are removed per row
    remaining_roses_per_row = ROSES_PER_ROW - red_roses_per_row

    # Calculate the number of white roses per row
    white_roses_per_row = remaining_roses_per_row * 3 / 5

    # Calculate the number of pink roses per row
    pink_roses_per_row = ROSES_PER_ROW - red_roses_per_row - white_roses_per_row

    # Calculate the total number of pink roses in the garden
    total_pink_roses = pink_roses_per_row * ROWS

    # Display the total number of pink roses
    result = total_pink_roses
    return result

print(solution())