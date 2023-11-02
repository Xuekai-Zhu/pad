def solution():
    """Mrs. Amaro has 80 roses in her garden. Three-fourths of her roses are red, one-fourth of the remaining are yellow, and the rest are white. How many of Mrs. Amaro's roses are either red or white?"""
    # Define the total number of roses
    total_roses = 80

    # Calculate the number of red roses
    red_roses = total_roses * 3/4

    # Calculate the number of remaining roses
    remaining_roses = total_roses - red_roses

    # Calculate the number of yellow roses
    yellow_roses = remaining_roses * 1/4

    # Calculate the number of white roses
    white_roses = total_roses - red_roses - yellow_roses

    # Calculate the number of red or white roses
    red_white_roses = red_roses + white_roses

    # return the result
    result = red_white_roses
    return result

print(solution())